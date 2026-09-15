import re
import random
import logging
from linebot.v3.messaging import TextMessage
from app.services.firebase_service import (
    record_task,
    list_tasks,
    claim_task,
    get_group_members,
    assign_roulette_task,
    get_unassigned_members
)
from app.utils.flex_templates import (
    create_main_menu_flex,
    create_help_flex,
    create_task_created_flex,
    create_task_list_flex,
    create_roulette_flex,
    create_preset_tasks_carousel,
    get_main_quick_reply
)

logger = logging.getLogger("leaderguard.command")

# 常見觸發主選單的問候與指令詞
MENU_KEYWORDS = {
    "選單", "menu", "Menu", "開始", "start", "嗨", "hi", "Hi",
    "hello", "Hello", "你好", "哈囉", "主選單", "功能選單"
}

def handle_user_command(user_text: str, group_id: str, user_id: str, user_name: str = "組員"):
    """
    解析並處理使用者輸入的指令
    回傳值：
        list of Messages (TextMessage 或 FlexMessage)，若非指令則回傳 None
    """
    text = user_text.strip()
    target_group = group_id or "default_group"

    # 1. 主選單指令（打招呼或輸入選單）
    if text in MENU_KEYWORDS:
        return [create_main_menu_flex()]

    # 2. 說明指南指令
    if text.lower() in ["/help", "help", "說明", "指令", "指令手冊", "幫助"]:
        return [create_help_flex()]

    # 3. 常用小組分工範本輪播卡片（點擊一鍵建立）
    if text.lower() in ["/task 範本", "/task template", "/template", "範本", "快速分工", "分工範本", "發起任務"]:
        return [create_preset_tasks_carousel()]

    # 4. 批次建立全套 4 大專案工作
    if text.lower() in ["/task 批次建立", "批次建立", "一鍵建立", "全部建立"]:
        presets = [
            ("簡報製作與美化", "負責PPT視覺美編與排版"),
            ("上台口頭報告", "負責掌握專案脈絡並代表口頭發表"),
            ("文獻查證與資料蒐集", "負責前期調研、文獻查證與數據整理"),
            ("書面報告撰寫統整", "負責期末書面Word/PDF格式與內容校對")
        ]
        for title, desc in presets:
            record_task(target_group, title, desc, user_id)
            
        tasks = list_tasks(target_group)
        return [
            TextMessage(text="已為本組建立 4 項常見專案工作，請組員在下方卡片點選「我負責」認領："),
            create_task_list_flex(tasks)
        ]

    # 5. 自訂任務建立：/task 新增 [名稱] [說明(選填)]
    if text.startswith("/task 新增") or text.startswith("/task add"):
        parts = re.split(r"\s+", text, maxsplit=3)
        if len(parts) < 3:
            return [TextMessage(text="指令格式：/task 新增 [任務名稱] [補充說明(選填)]\n\n例如：\n/task 新增 製作問卷 負責設計 Google 表單並回收數據")]
        
        title = parts[2]
        description = parts[3] if len(parts) > 3 else ""
        
        task_id = record_task(target_group, title, description, user_id)
        return [create_task_created_flex(task_id, title, description, user_name)]

    # 6. 任務清單：/task 清單 或 /tasks
    if text in ["/task 清單", "/task list", "/tasks", "任務清單"]:
        tasks = list_tasks(target_group)
        return [create_task_list_flex(tasks)]

    # 7. 主動認領任務：/claim [任務ID]
    if text.startswith("/claim") or text.startswith("/認領"):
        parts = re.split(r"\s+", text)
        if len(parts) < 2:
            return [TextMessage(text="請輸入要認領的任務編號，例如：/claim T001")]
        
        task_id = parts[1].upper()
        success, title = claim_task(task_id, user_id, user_name)
        if success:
            return [TextMessage(text=f"認領完成！\n【{task_id}】{title}\n由「{user_name}」負責。\n已記錄認領時間與進度，期末互評有憑有據。")]
        else:
            return [TextMessage(text=f"找不到待認領的任務「{task_id}」，或這項工作已經有人負責了。")]

    # 8. 隨機抽籤分工：/roulette 或 /抽籤 或 /輪盤（僅抽還沒有工作任務的人）
    if text.lower() in ["/roulette", "/輪盤", "/抽籤", "抽籤", "隨機分工", "死鬥輪盤"]:
        free_members, all_members, all_tasks, pending_tasks = get_unassigned_members(target_group)
        
        # 情況 A：尚未建立任何任務
        if not all_tasks:
            return [TextMessage(text="目前還沒有建立任何任務，請先點選「常用分工範本」或使用「/task 新增」建立工作後再進行抽籤。")]
        
        # 情況 B：所有任務皆已被認領
        if not pending_tasks:
            return [TextMessage(text="目前所有任務都已經有人負責了，不需要抽籤。")]
            
        # 情況 C：優先從「尚未有任何任務」的人選中抽籤
        if free_members:
            victim = random.choice(free_members)
        elif all_members:
            victim = random.choice(all_members)
        else:
            victim = {"user_id": user_id, "user_name": user_name}

        task_id, task_title = assign_roulette_task(target_group, victim["user_id"], victim["user_name"])
        return [create_roulette_flex(task_id, task_title, victim["user_name"])]

    # 9. 當前群組狀態：/status
    if text.lower() in ["/status", "狀態", "進度"]:
        pending_count = len(list_tasks(target_group, status="pending"))
        claimed_count = len(list_tasks(target_group, status="claimed"))
        
        status_msg = (
            f"【目前專案分工進度】\n\n"
            f"待認領任務：{pending_count} 件\n"
            f"進行中任務：{claimed_count} 件\n\n"
            f"輸入「/task 清單」查看詳細項目\n"
            f"輸入「/roulette」隨機抽籤分配未認領工作"
        )
        return [TextMessage(text=status_msg, quick_reply=get_main_quick_reply())]

    # 非指令，回傳 None
    return None

