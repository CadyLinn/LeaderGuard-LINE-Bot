import re
import random
import logging
from linebot.v3.messaging import TextMessage
from app.services.firebase_service import (
    record_task,
    list_tasks,
    claim_task,
    delete_task,
    get_group_members,
    assign_roulette_task,
    get_unassigned_members,
    add_manual_member,
    set_manual_members,
    clear_manual_members
)
from app.utils.flex_templates import (
    create_main_menu_flex,
    create_help_flex,
    create_task_created_flex,
    create_task_list_flex,
    create_task_delete_flex,
    create_roulette_flex,
    create_preset_tasks_carousel,
    create_welcome_guide_flex,
    create_upgrade_plan_flex,
    create_upgrade_success_flex,
    create_ai_reminder_flex,
    create_invite_group_flex,
    get_main_quick_reply
)

logger = logging.getLogger("leaderguard.command")

def get_invite_group_guide_text() -> str:
    """產生引導用戶將組長保險加入小組群組的文字說明"""
    return (
        "【如何將「組長保險」加入小組群組】\n\n"
        "只要簡單 3 步驟，即可將「組長保險」邀請進報告群組，協助小組落實工作分工與進度追蹤：\n\n"
        "1. 開啟 LINE 小組群組\n"
        "點開群組聊天室，進入您的大學報告或專案小組群組。\n\n"
        "2. 點擊右上角選單（≡）> 點選「邀請」\n"
        "點群組右上角的選單按鈕（≡ 三條線），進入群組功能頁後點選「邀請」圖示。\n\n"
        "3. 搜尋並加入「組長保險」\n"
        "在好友清單搜尋欄輸入「組長保險」，勾選後點擊右上角「邀請」，機器人就會立即進駐群組！\n\n"
        "―――\n"
        "【進群後的第一步】\n"
        "• 輸入「/選單」：隨時喚起小組專案管理中心\n"
        "• 輸入「/task 範本」：建立簡報、報告、調研、書面等常見分工\n"
        "• 輸入「/抽籤」：尚未認領的工作，交由系統隨機分配指派\n\n"
        "若要推薦給同學或組員，也可直接轉傳官方帳號連結：\n"
        "https://line.me/R/nv/recommendOA/@805yffpw"
    )

# 常見觸發主選單的問候與指令詞
MENU_KEYWORDS = {
    "/menu", "/選單", "/主選單", "/開始", "/start",
    "選單", "menu", "Menu", "開始", "start", "嗨", "hi", "Hi",
    "hello", "Hello", "你好", "哈囉", "主選單", "功能選單"
}

def handle_user_command(user_text: str, group_id: str, user_id: str, user_name: str = "組員"):
    """
    解析並處理使用者輸入的指令（支援「/」後接中文或英文指令）
    回傳值：
        list of Messages (TextMessage 或 FlexMessage)，若非指令則回傳 None
    """
    # 支援全形「／」轉換為半形「/」，並去除首尾空白
    text = user_text.strip().replace("／", "/")
    target_group = group_id or "default_group"

    # 1. 主選單指令（中英文皆可）
    if text in MENU_KEYWORDS or text.lower() in ["/menu", "/start", "menu", "start"]:
        return [create_main_menu_flex()]

    # 2. 常用指令說明指令（/常用指令說明、/help 或 /說明）
    if text.lower() in [
        "/常用指令說明", "常用指令說明",
        "/常用指令", "常用指令",
        "/指令說明", "指令說明",
        "/help", "help",
        "/說明", "說明",
        "/指令", "指令",
        "/指令手冊", "指令手冊",
        "/輸入指令", "輸入指令",
        "/幫助", "幫助",
        "/指南", "指南"
    ]:
        return [create_help_flex()]

    # 2.2 如何將組長保險加入群組說明（文字教學說明）
    if text.lower() in [
        "/如何加入群組", "如何加入群組",
        "/加入群組說明", "加入群組說明",
        "/加入群組教學", "加入群組教學",
        "/加入群組", "加入群組",
        "/加到群組", "加到群組",
        "/邀請", "邀請",
        "/邀請機器人", "邀請機器人",
        "/邀請教學", "邀請教學",
        "/加群步驟", "加群步驟",
        "/加群教學", "加群教學",
        "/加群", "加群",
        "/拉進群組", "拉進群組",
        "/邀進群組", "邀進群組"
    ]:
        return [TextMessage(text=get_invite_group_guide_text())]

    # 2.3 立即把組長保險加入群組圖卡
    if text.lower() in [
        "/加入群組圖卡", "加入群組圖卡",
        "/加群圖卡", "加群圖卡",
        "/邀請圖卡", "邀請圖卡"
    ]:
        return [create_invite_group_flex()]

    # 2.5 4 步驟使用手冊（/手冊、/使用手冊、/4步驟 或 /guide）
    if text.lower() in [
        "/手冊", "手冊", "/使用手冊", "使用手冊", "/4步驟", "4步驟", "/guide", "guide"
    ]:
        return [create_welcome_guide_flex()]

    # 2.8 升級方案卡片（/升級方案、/升級、/upgrade 或 /方案）
    if text.lower() in [
        "/升級方案", "升級方案",
        "/升級", "升級",
        "/了解pro專案", "了解pro專案",
        "/了解pro方案", "了解pro方案",
        "/保險單次包", "保險單次包",
        "/組長躺平pass", "組長躺平pass",
        "/組長躺平", "組長躺平",
        "/方案", "方案",
        "/upgrade", "upgrade",
        "/諮詢升級", "諮詢升級",
        "/pro", "pro"
    ]:
        return [create_upgrade_plan_flex()]

    # 2.9 競賽 DEMO 一鍵體驗 PRO 尊榮升級（/體驗升級、/一鍵升級、/立即升級、/升級解鎖）
    if text.lower() in [
        "/體驗升級", "體驗升級",
        "/一鍵升級", "一鍵升級",
        "/立即升級", "立即升級",
        "/升級體驗", "升級體驗",
        "/升級解鎖", "升級解鎖",
        "/解鎖pro", "解鎖pro",
        "/pro解鎖", "pro解鎖",
        "/體驗pro", "體驗pro"
    ]:
        return [create_upgrade_success_flex()]

    # 2.95 進度提醒通知（/催繳、/催繳 正式、/提醒）
    if text.lower().startswith("/催繳") or text.lower().startswith("催繳") or text.lower().startswith("/提醒") or text.lower().startswith("提醒"):
        mode = "formal" if any(kw in text.lower() for kw in ["正式", "期限", "里程碑", "教授", "稽核", "通報"]) else "friendly"
        tasks = list_tasks(target_group)
        pending_tasks = [t for t in tasks if t.get("status") == "pending"]
        return [create_ai_reminder_flex(pending_tasks=pending_tasks, mode=mode)]

    # 3. 常用小組分工範本輪播卡片（/assign、/task 範本 或 /任務 範本）
    if text.lower() in [
        "/assign", "/指派", "/指派任務", "assign", "指派",
        "/task 範本", "/task template", "/template", "範本", "快速分工", "分工範本", "發起任務",
        "/任務 範本", "/任務 template", "/任務範本"
    ]:
        return [create_preset_tasks_carousel()]

    # 4. 批次建立全套 4 大專案工作（/task 批次建立 或 /任務 批次建立）
    if text.lower() in [
        "/task 批次建立", "/task batch", "批次建立", "一鍵建立", "全部建立",
        "/任務 批次建立", "/任務 batch", "/任務 全部建立", "/任務 一鍵建立"
    ]:
        presets = [
            ("簡報製作與美化", "負責PPT視覺美編與排版", ["簡報", "ppt", "canva", "slides", "投影片"]),
            ("上台口頭報告", "負責掌握專案脈絡並代表口頭發表", ["口頭報告", "上台報告", "口頭發表", "上台發表", "口頭"]),
            ("文獻查證與資料蒐集", "負責前期調研、文獻查證與數據整理", ["文獻", "資料蒐集", "資料收集", "文獻查證", "調研"]),
            ("書面報告撰寫統整", "負責期末書面Word/PDF格式與內容校對", ["書面報告", "書面撰寫", "報告統整", "書面統整", "報告撰寫"])
        ]
        
        existing_tasks = list_tasks(target_group)
        existing_titles = [t.get("title", "").strip().lower() for t in existing_tasks]
        
        def is_already_exists(p_title, keywords):
            p_lower = p_title.lower()
            for ext in existing_titles:
                if ext == p_lower or ext in p_lower or p_lower in ext:
                    return True
                for kw in keywords:
                    if kw.lower() in ext:
                        return True
            return False

        added_tasks = []
        skipped_tasks = []
        for title, desc, kws in presets:
            if is_already_exists(title, kws):
                skipped_tasks.append(title)
            else:
                record_task(target_group, title, desc, user_id)
                added_tasks.append(title)
                
        tasks = list_tasks(target_group)
        
        if not added_tasks:
            msg = "小組 4 大常見專案工作先前均已建立，已為您自動略過重複項目。請直接在下方查看任務清單："
        elif skipped_tasks:
            skipped_str = "、".join(skipped_tasks)
            msg = f"已為本組建立 {len(added_tasks)} 項專案工作（已自動略過重複的「{skipped_str}」），請組員在下方卡片點選「我負責」認領："
        else:
            msg = "已為本組建立 4 項常見專案工作，請組員在下方卡片點選「我負責」認領："

        return [
            TextMessage(text=msg, quick_reply=get_main_quick_reply()),
            create_task_list_flex(tasks)
        ]

    # 5. 自訂任務建立：/task 新增 [名稱] [說明] 或 /任務 新增 [名稱] [說明]
    task_add_prefixes = (
        "/task 新增", "/task add",
        "/任務 新增", "/任務 add",
        "/新增任務", "任務 新增", "task add"
    )
    matched_task_add = None
    for pfx in task_add_prefixes:
        if text.startswith(pfx):
            matched_task_add = pfx
            break

    if matched_task_add:
        content = text[len(matched_task_add):].strip()
        parts = re.split(r"\s+", content, maxsplit=1)
        if not parts or not parts[0]:
            return [TextMessage(
                text="指令格式：\n• /task 新增 [任務名稱] [補充說明(選填)]\n• /任務 新增 [任務名稱] [補充說明(選填)]\n\n例如：\n/任務 新增 製作問卷 負責設計 Google 表單並回收數據",
                quick_reply=get_main_quick_reply()
            )]
        
        title = parts[0]
        description = parts[1] if len(parts) > 1 else ""
        
        # 檢查是否已存在相同名稱的任務，避免重複點擊重複新增
        existing_tasks = list_tasks(target_group)
        if any(t.get("title", "").strip().lower() == title.lower() for t in existing_tasks):
            return [
                TextMessage(
                    text=f"任務「{title}」已經在群組清單中囉！請直接在下方任務清單中認領，避免重複建立。",
                    quick_reply=get_main_quick_reply()
                ),
                create_task_list_flex(existing_tasks)
            ]
        
        task_id = record_task(target_group, title, description, user_id)
        return [create_task_created_flex(task_id, title, description, user_name)]

    # 5.5 刪除任務：/task 刪除 [編號/名稱] 或 /任務 刪除 [編號/名稱] 或 /刪除 [編號/名稱]
    task_del_prefixes = (
        "/task 刪除", "/task delete", "/task del", "/task rm",
        "/任務 刪除", "/任務 delete", "/任務 del",
        "/刪除任務", "/刪除工作", "任務 刪除", "task delete"
    )
    matched_task_del = None
    for pfx in task_del_prefixes:
        if text.lower().startswith(pfx):
            matched_task_del = pfx
            break

    is_standalone_del = False
    del_arg = ""
    if matched_task_del:
        del_arg = text[len(matched_task_del):].strip()
    elif text.lower().startswith("/刪除") or text.lower().startswith("/delete") or text.lower().startswith("/del"):
        parts = text.split(maxsplit=1)
        if parts[0].lower() in ["/刪除", "/delete", "/del"]:
            is_standalone_del = True
            del_arg = parts[1].strip() if len(parts) > 1 else ""

    if matched_task_del or is_standalone_del:
        if not del_arg:
            tasks = list_tasks(target_group)
            if not tasks:
                return [TextMessage(text="目前群組內沒有任何工作，無需刪除。", quick_reply=get_main_quick_reply())]
            return [create_task_delete_flex(tasks)]

        success, deleted_task = delete_task(target_group, del_arg)
        if success:
            d_id = deleted_task.get("id", del_arg)
            d_title = deleted_task.get("title", "")
            remaining_tasks = list_tasks(target_group)
            msg = f"已成功刪除工作：【{d_id}】{d_title}。"
            if remaining_tasks:
                return [
                    TextMessage(text=f"{msg}\n以下為目前小組最新工作清單：", quick_reply=get_main_quick_reply()),
                    create_task_list_flex(remaining_tasks)
                ]
            else:
                return [
                    TextMessage(text=f"{msg}\n目前群組內已無任何待辦工作，如需分工可點選下方「常用分工範本」或「自訂新增工作」。", quick_reply=get_main_quick_reply())
                ]
        else:
            return [
                TextMessage(
                    text=f"找不到符合「{del_arg}」的工作，請確認編號是否正確（例如 T001）。\n可輸入「/task 刪除」開啟刪除清單直接點選按鈕。",
                    quick_reply=get_main_quick_reply()
                )
            ]

    # 6. 任務清單：/task 清單、/任務 清單、/tasks 或 /任務
    if text.lower() in [
        "/task 清單", "/task list", "/tasks", "/task",
        "/任務 清單", "/任務 list", "/任務", "/清單",
        "任務清單", "任務", "tasks", "task"
    ]:
        tasks = list_tasks(target_group)
        return [create_task_list_flex(tasks)]

    # 7. 主動認領任務：/claim [任務ID] 或 /認領 [任務ID]
    claim_match = re.match(r"^(?:/claim|/認領|/負責|claim|認領|我負責)\s*(.*)$", text, re.IGNORECASE)
    if claim_match and (text.startswith("/") or text.lower().startswith("claim") or text.startswith("認領") or text.startswith("我負責")):
        arg = claim_match.group(1).strip()
        if not arg:
            return [TextMessage(text="請輸入要認領的任務編號，例如：/claim T001 或 /認領 T001", quick_reply=get_main_quick_reply())]
        
        task_id = arg.split()[0].upper()
        success, title = claim_task(task_id, user_id, user_name)
        if success:
            return [TextMessage(text=f"認領完成！\n【{task_id}】{title}\n由「{user_name}」負責。\n已記錄認領時間與進度，期末互評有憑有據。", quick_reply=get_main_quick_reply())]
        else:
            return [TextMessage(text=f"找不到待認領的任務「{task_id}」，或這項工作已經有人負責了。", quick_reply=get_main_quick_reply())]

    # 8. 隨機抽籤分工：/roulette 或 /抽籤 或 /輪盤（支援附加名單，例如 /抽籤 小明 小華 小美）
    roulette_prefixes = [
        "/roulette", "/輪盤", "/抽籤", "/隨機分工", "/隨機抽籤", "/隨機分配", "/命運抽籤",
        "roulette", "輪盤", "抽籤", "隨機分工", "隨機抽籤", "隨機分配", "命運抽籤"
    ]
    is_roulette_cmd = False
    roulette_arg = ""
    for r_pfx in roulette_prefixes:
        if text.lower() == r_pfx:
            is_roulette_cmd = True
            break
        elif text.lower().startswith(r_pfx + " ") or text.lower().startswith(r_pfx + "：") or text.lower().startswith(r_pfx + ":"):
            is_roulette_cmd = True
            roulette_arg = text[len(r_pfx):].strip(" ：:")
            break

    if is_roulette_cmd:
        # 若抽籤指令直接附帶了組員名單，例如「/抽籤 小明, 小華, 小美」，自動將其登記為群組名冊
        if roulette_arg:
            inline_names = [n.strip() for n in re.split(r"[,，、\s\n]+", roulette_arg) if n.strip()]
            if inline_names:
                set_manual_members(target_group, inline_names, replace=True)

        free_members, all_members, all_tasks, pending_tasks = get_unassigned_members(target_group)
        
        # 情況 A：尚未建立任何任務
        if not all_tasks:
            return [TextMessage(text="目前還沒有建立任何任務，請先點選「常用分工範本」或使用「/任務 新增」建立工作後再進行隨機分配。", quick_reply=get_main_quick_reply())]
        
        # 情況 B：所有任務皆已被認領
        if not pending_tasks:
            return [TextMessage(text="目前所有任務都已經有人負責了，無需隨機分配。", quick_reply=get_main_quick_reply())]
            
        # 情況 C：優先從「尚未有任何任務」的人選中抽籤
        if free_members:
            victim = random.choice(free_members)
        elif all_members:
            victim = random.choice(all_members)
        else:
            victim = {"user_id": user_id, "user_name": user_name}

        task_id, task_title = assign_roulette_task(target_group, victim["user_id"], victim["user_name"])
        roulette_card = create_roulette_flex(task_id, task_title, victim["user_name"])

        # 如果已知組員只有 1 人（即傳訊息的人），額外附上提示教學，讓組長知道如何設定名單
        if len(all_members) <= 1:
            notice_text = (
                "【隨機分配小提示】\n"
                "目前群組名冊僅有您 1 人，因此隨機分配會指派給目前發送訊息者。\n\n"
                "組長可直接在群組發送：\n"
                "「/組員 姓名1, 姓名2, 姓名3, 姓名4」\n"
                "登記全體組員姓名後，下次即可在全體名冊中進行隨機指派！"
            )
            return [roulette_card, TextMessage(text=notice_text, quick_reply=get_main_quick_reply())]

        return [roulette_card]

    # 9. 當前群組狀態：/status 或 /狀態 或 /進度
    if text.lower() in ["/status", "/狀態", "/進度", "status", "狀態", "進度"]:
        pending_count = len(list_tasks(target_group, status="pending"))
        claimed_count = len(list_tasks(target_group, status="claimed"))
        
        status_msg = (
            f"【目前專案分工進度】\n\n"
            f"待認領任務：{pending_count} 件\n"
            f"進行中任務：{claimed_count} 件\n\n"
            f"輸入「/task 清單」查看詳細項目\n"
            f"輸入「/抽籤」隨機分配未認領工作"
        )
        return [TextMessage(text=status_msg, quick_reply=get_main_quick_reply())]

    # 9.5 期末專案報告匯出：/export 或 /匯出
    if text.lower() in ["/export", "/匯出", "/報告", "/結案報告", "export", "匯出"]:
        tasks = list_tasks(target_group)
        free_members, all_members, _, _ = get_unassigned_members(target_group)
        
        claimed_tasks = [t for t in tasks if t.get("status") == "claimed"]
        pending_tasks = [t for t in tasks if t.get("status") == "pending"]
        
        lines = [
            "【組長保險・小組專案分工與成果存證報告】\n",
            "存證狀態：已記錄系統時間戳記與各成員分工明細",
            f"專案任務總數：{len(tasks)} 件",
            f"已認領負責：{len(claimed_tasks)} 件",
            f"待認領工作：{len(pending_tasks)} 件\n",
            "【各組員負責項目與工作存證】"
        ]
        
        member_tasks = {}
        for t in claimed_tasks:
            name = t.get("assignee_name", "組員")
            member_tasks.setdefault(name, []).append(f"[{t.get('id', '')}] {t.get('title', '')}")
            
        if member_tasks:
            for name, t_list in member_tasks.items():
                lines.append(f"• {name}（共負責 {len(t_list)} 項）：")
                for item in t_list:
                    lines.append(f"   - {item}")
        else:
            lines.append("（目前尚無組員完成任務認領）")
            
        if free_members:
            free_names = [m.get("user_name", "組員") for m in free_members]
            lines.append(f"\n【尚未指派工作之組員】：\n{', '.join(free_names)}")
            
        lines.append("\n本紀錄由組長保險系統自動生成，具備系統時間戳記，可作為期末成果報告與互評參考依據。")
        return [TextMessage(text="\n".join(lines), quick_reply=get_main_quick_reply())]

    # 10. 清空手動登記組員名冊：/組員 清空、/清空名單、/清空組員
    if text.lower() in [
        "/組員 清空", "/成員 清空", "/名單 清空",
        "/清空組員", "/清空名單", "/清空成員",
        "組員 清空", "清空組員", "清空名單"
    ]:
        removed = clear_manual_members(target_group)
        return [TextMessage(
            text=(
                "【小組成員名冊已清空】\n\n"
                f"已清除先前登記的手動組員名單（共 {removed} 筆）。\n"
                "組長可隨時輸入：\n"
                "「/組員 姓名1, 姓名2, 姓名3...」\n"
                "重新登記全體組員！"
            ),
            quick_reply=get_main_quick_reply()
        )]

    # 10.5 設定/新增成員名單：支援「/組員 小明, 小華, 小美」、「/設定組員 小明 小華」或「/組員 新增 小明」
    member_set_prefixes = (
        "/組員", "/成員", "/名單",
        "/設定組員", "/設定名單", "/組員名單",
        "/member", "/members"
    )
    matched_set_prefix = None
    for pfx in member_set_prefixes:
        if text.startswith(pfx + " ") or text.startswith(pfx + "：") or text.startswith(pfx + ":") or text.startswith(pfx + "\n"):
            matched_set_prefix = pfx
            break

    if matched_set_prefix:
        raw_args = text[len(matched_set_prefix):].strip(" ：:\n\t")
        # 判斷是否帶有「新增」關鍵字
        is_append = False
        if re.match(r"^(新增|add)\b", raw_args, re.I):
            is_append = True
            raw_args = re.sub(r"^(新增|add)\s*", "", raw_args, flags=re.I).strip()
            
        names = [n.strip() for n in re.split(r"[,，、\s\n]+", raw_args) if n.strip()]
        if not names:
            return [TextMessage(
                text=(
                    "【組長登記組員名單教學】\n\n"
                    "指令範例：\n"
                    "• /組員 小明, 小華, 小美, 大寶\n"
                    "• /組員 小明 小華 小美 大寶\n"
                    "• /組員 小明、小華、小美、大寶\n\n"
                    "登記後輸入「/抽籤」即可在全體名冊中公平隨機分配任務！"
                ),
                quick_reply=get_main_quick_reply()
            )]
            
        added = set_manual_members(target_group, names, replace=(not is_append))
        all_members = get_group_members(target_group)
        
        member_list_str = "\n".join([f"{idx+1}. {m['user_name']}" for idx, m in enumerate(all_members)])
        reply_msg = (
            f"【小組成員名冊設定完成】\n\n"
            f"已成功登記 {len(all_members)} 位組員：\n"
            f"{member_list_str}\n\n"
            "【隨機分配指引】：\n"
            "• 輸入「/抽籤」即可在全體名冊中進行隨機分配。\n"
            "• 系統優先分配尚未認領工作的成員，避免重複承擔。\n"
            "• 輸入「/組員」檢視名冊，輸入「/組員 清空」可重設名冊。"
        )
        return [TextMessage(text=reply_msg, quick_reply=get_main_quick_reply())]

    # 11. 查看群組成員名冊與狀態：/member、/成員、/組員 或 /名單
    if text.lower() in [
        "/member", "/member 清單", "/member list",
        "/成員", "/成員 清單", "/成員 list",
        "/組員", "/組員 清單",
        "/名單", "/名單 清單",
        "member", "成員", "組員", "名單", "組員名單"
    ]:
        free_members, all_members, all_tasks, _ = get_unassigned_members(target_group)
        if not all_members:
            return [TextMessage(
                text=(
                    "【小組成員名冊】\n"
                    "目前群組尚未登記組員名單。\n\n"
                    "【組長登記組員指引】：\n"
                    "直接在群組發送：\n"
                    "「/組員 姓名1, 姓名2, 姓名3...」\n\n"
                    "例如：\n"
                    "/組員 小明, 小華, 小美, 大寶\n\n"
                    "登記後輸入「/抽籤」即可由全體組員進行隨機分配！"
                ),
                quick_reply=get_main_quick_reply()
            )]
            
        task_map = {}
        for t in all_tasks:
            if t.get("status") == "claimed" and t.get("assignee_name"):
                task_map[t["assignee_name"]] = t.get("title", "")
            elif t.get("status") == "claimed" and t.get("assignee_id"):
                task_map[t["assignee_id"]] = t.get("title", "")

        lines = ["【小組成員與任務現況】"]
        for m in all_members:
            uid = m.get("user_id", "")
            uname = m.get("user_name", "組員")
            if uname in task_map:
                lines.append(f"• {uname}：負責「{task_map[uname]}」")
            elif uid in task_map:
                lines.append(f"• {uname}：負責「{task_map[uid]}」")
            else:
                lines.append(f"• {uname}：尚未分配任務（抽籤候選）")
                
        if len(all_members) <= 1:
            lines.append("\n提示：目前名冊只有 1 人，組長可輸入「/組員 姓名1, 姓名2, 姓名3」一次登記全體組員名單。")
        else:
            lines.append("\n• 輸入「/抽籤」：隨機分配未認領工作\n• 輸入「/組員 清空」：重設成員名冊")
            
        return [TextMessage(text="\n".join(lines), quick_reply=get_main_quick_reply())]

    # 12. 成員手動簽到：/checkin、/簽到 或 /報到
    if text.lower() in ["/checkin", "/簽到", "/報到", "checkin", "簽到", "報到", "+1"]:
        return [TextMessage(text=f"「{user_name}」簽到成功！已將您登記至小組名冊。", quick_reply=get_main_quick_reply())]

    # 非指令，回傳 None
    return None


