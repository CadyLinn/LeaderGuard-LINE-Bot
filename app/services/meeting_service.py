import os
import json
import logging
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("leaderguard.meeting")

# 群組會議狀態與歷史紀錄（記憶體持久化，可切換至 Firebase）
# active_meetings[group_id] = {
#     "starter_id": str,
#     "starter_name": str,
#     "start_time": str,
#     "messages": [{"time": str, "user_name": str, "text": str}]
# }
active_meetings = {}
meeting_history = {}
unlocked_pro_groups = set()

# 初始化 Gemini API
GEMINI_KEY = os.getenv("GEMINI_API_KEY", "")
gemini_model = None

if GEMINI_KEY:
    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_KEY)
        # 使用最新支援的 gemini-3.6-flash
        gemini_model = genai.GenerativeModel("models/gemini-3.6-flash")
        logger.info("Gemini API 模型已成功初始化 (models/gemini-3.6-flash)")
    except Exception as e:
        logger.warning(f"Gemini API 初始化失敗: {e}")

def unlock_pro_for_group(group_id: str) -> bool:
    """付款解鎖群組之 PRO 會議記錄功能"""
    target = group_id or "default_group"
    unlocked_pro_groups.add(target)
    return True

def is_pro_unlocked(group_id: str) -> bool:
    """檢查該群組是否已解鎖 PRO 功能（競賽展示預設視為已開通）"""
    return True

def is_meeting_active(group_id: str) -> bool:
    """檢查群組是否正在進行會議"""
    target = group_id or "default_group"
    return target in active_meetings

def start_meeting(group_id: str, user_id: str, user_name: str) -> tuple[bool, str, dict]:
    """開始群組會議並啟動對話記錄"""
    target = group_id or "default_group"
    if target in active_meetings:
        meeting = active_meetings[target]
        return False, f"目前會議已在進行中（由 {meeting['starter_name']} 於 {meeting['start_time']} 發起）。\n如要統整記錄，請輸入「/結束會議」。", meeting

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    meeting_data = {
        "group_id": target,
        "starter_id": user_id,
        "starter_name": user_name or "組員",
        "start_time": now_str,
        "messages": []
    }
    active_meetings[target] = meeting_data
    logger.info(f"群組 {target} 開始會議，發起人: {user_name}")
    return True, "會議記錄已成功啟動！", meeting_data

def record_meeting_message(group_id: str, user_id: str, user_name: str, text: str):
    """在會議進行中記錄成員發言（忽略系統指令）"""
    target = group_id or "default_group"
    if target not in active_meetings:
        return

    clean_text = text.strip()
    if clean_text.startswith("/") or clean_text.startswith("／"):
        return

    time_str = datetime.now().strftime("%H:%M")
    active_meetings[target]["messages"].append({
        "time": time_str,
        "user_id": user_id,
        "user_name": user_name or "組員",
        "text": clean_text
    })

def end_meeting(group_id: str, user_id: str, user_name: str) -> tuple[bool, str, dict]:
    """結束會議並使用 Gemini API 統整會議記錄"""
    target = group_id or "default_group"
    if target not in active_meetings:
        return False, "目前群組尚未開始會議。\n請輸入「/開始會議」啟動記錄。", {}

    meeting = active_meetings.pop(target)
    meeting["end_time"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    meeting["ender_name"] = user_name or "組員"

    messages = meeting.get("messages", [])
    summary_data = generate_ai_meeting_summary(meeting, messages)

    # 存入歷史紀錄
    meeting_history.setdefault(target, []).append({
        "info": meeting,
        "summary": summary_data
    })

    return True, "會議已結束，AI 統整記錄完成！", summary_data

def generate_ai_meeting_summary(meeting_info: dict, messages: list) -> dict:
    """呼叫 Gemini API 統整對話內容，若 API 無回應則啟用智能規則回退"""
    if not messages:
        return {
            "title": "小組專案會議",
            "start_time": meeting_info.get("start_time", ""),
            "end_time": meeting_info.get("end_time", ""),
            "starter_name": meeting_info.get("starter_name", "組員"),
            "msg_count": 0,
            "summary_points": ["會議期間未擷取到有效文字發言。"],
            "decisions": ["無特別決議事項。"],
            "action_items": []
        }

    # 組合對話文字
    dialogue_lines = []
    for m in messages:
        dialogue_lines.append(f"[{m['time']}] {m['user_name']}: {m['text']}")
    dialogue_text = "\n".join(dialogue_lines)

    if gemini_model:
        prompt = (
            "你是一個專業的大學專案小組協作秘書。以下是一段會議期間組員在 LINE 群組的即時討論紀錄：\n\n"
            f"{dialogue_text}\n\n"
            "請分析上述對話，並以純 JSON 格式輸出摘要報告，格式必須嚴格符合以下結構，不要加入 markdown 標記（如 ```json 等）：\n"
            "{\n"
            '  "title": "會議核心主題（15字以內）",\n'
            '  "summary_points": ["討論重點1", "討論重點2", "討論重點3"],\n'
            '  "decisions": ["小組決議事項1", "小組決議事項2"],\n'
            '  "action_items": [{"task": "待辦工作名稱", "assignee": "負責人姓名（若未指定則填「待認領」）"}]\n'
            "}\n"
            "規範：請使用繁體中文，語氣簡潔專業、客觀清晰，不要包含任何 emoji。"
        )

        try:
            resp = gemini_model.generate_content(prompt)
            raw_text = resp.text.strip()
            # 清理可能夾帶的 ```json 與 ```
            if raw_text.startswith("```"):
                lines = raw_text.split("\n")
                if lines[0].startswith("```"):
                    lines = lines[1:]
                if lines and lines[-1].startswith("```"):
                    lines = lines[:-1]
                raw_text = "\n".join(lines).strip()

            parsed = json.loads(raw_text)
            parsed["start_time"] = meeting_info.get("start_time", "")
            parsed["end_time"] = meeting_info.get("end_time", "")
            parsed["starter_name"] = meeting_info.get("starter_name", "組員")
            parsed["msg_count"] = len(messages)
            return parsed
        except Exception as err:
            logger.error(f"Gemini API 生成會議摘要解析失敗，改用智能回退處理: {err}")

    # 智能備份處理（當無 API 金鑰或網路連線失敗時保證不當機）
    return fallback_summary(meeting_info, messages)

def fallback_summary(meeting_info: dict, messages: list) -> dict:
    """智能規則萃取會議重點與待辦清單"""
    summary_points = []
    decisions = []
    action_items = []

    unique_speakers = list(dict.fromkeys([m["user_name"] for m in messages]))
    summary_points.append(f"參與討論成員：{', '.join(unique_speakers[:5])}")

    # 關鍵字篩選
    for m in messages:
        text = m["text"]
        uname = m["user_name"]
        if any(kw in text for kw in ["做", "負責", "寫", "畫", "弄", "交給", "負責製作"]):
            action_items.append({"task": text[:20], "assignee": uname})
        elif any(kw in text for kw in ["決定", "定在", "結論", "確定", "就這樣", "同意"]):
            decisions.append(text[:25])
        elif len(text) > 8 and len(summary_points) < 4:
            summary_points.append(f"{uname}：{text[:30]}")

    if not summary_points:
        summary_points.append("會議討論專案分工與執行進度。")
    if not decisions:
        decisions.append("確認各項工作依既定日程推進。")

    return {
        "title": "小組專案進度與分工會議",
        "start_time": meeting_info.get("start_time", ""),
        "end_time": meeting_info.get("end_time", ""),
        "starter_name": meeting_info.get("starter_name", "組員"),
        "msg_count": len(messages),
        "summary_points": summary_points[:3],
        "decisions": decisions[:2],
        "action_items": action_items[:4]
    }
