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
    add_manual_member
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
    get_main_quick_reply
)

logger = logging.getLogger("leaderguard.command")

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

    # 2.5 4 步驟使用手冊（/手冊、/使用手冊、/4步驟 或 /guide）
    if text.lower() in [
        "/手冊", "手冊", "/使用手冊", "使用手冊", "/4步驟", "4步驟", "/guide", "guide"
    ]:
        return [create_welcome_guide_flex()]

    # 2.8 升級方案卡片（/升級方案、/升級、/upgrade 或 /方案）
    if text.lower() in [
        "/升級方案", "升級方案",
        "/升級", "升級",
        "/立即升級", "立即升級",
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

    # 8. 隨機抽籤分工：/roulette 或 /抽籤 或 /輪盤（僅抽還沒有工作任務的人）
    if text.lower() in [
        "/roulette", "/輪盤", "/抽籤", "/隨機分工", "/隨機抽籤", "/死鬥輪盤", "/命運抽籤",
        "roulette", "輪盤", "抽籤", "隨機分工", "隨機抽籤", "死鬥輪盤", "命運抽籤"
    ]:
        free_members, all_members, all_tasks, pending_tasks = get_unassigned_members(target_group)
        
        # 情況 A：尚未建立任何任務
        if not all_tasks:
            return [TextMessage(text="目前還沒有建立任何任務，請先點選「常用分工範本」或使用「/任務 新增」建立工作後再進行抽籤。", quick_reply=get_main_quick_reply())]
        
        # 情況 B：所有任務皆已被認領
        if not pending_tasks:
            return [TextMessage(text="目前所有任務都已經有人負責了，不需要抽籤。", quick_reply=get_main_quick_reply())]
            
        # 情況 C：優先從「尚未有任何任務」的人選中抽籤
        if free_members:
            victim = random.choice(free_members)
        elif all_members:
            victim = random.choice(all_members)
        else:
            victim = {"user_id": user_id, "user_name": user_name}

        task_id, task_title = assign_roulette_task(target_group, victim["user_id"], victim["user_name"])
        return [create_roulette_flex(task_id, task_title, victim["user_name"])]

    # 9. 當前群組狀態：/status 或 /狀態 或 /進度
    if text.lower() in ["/status", "/狀態", "/進度", "status", "狀態", "進度"]:
        pending_count = len(list_tasks(target_group, status="pending"))
        claimed_count = len(list_tasks(target_group, status="claimed"))
        
        status_msg = (
            f"【目前專案分工進度】\n\n"
            f"待認領任務：{pending_count} 件\n"
            f"進行中任務：{claimed_count} 件\n\n"
            f"輸入「/task 清單」或「/任務 清單」查看詳細項目\n"
            f"輸入「/命運抽籤」或「/roulette」隨機抽籤分配未認領工作"
        )
        return [TextMessage(text=status_msg, quick_reply=get_main_quick_reply())]

    # 9.5 期末專案報告匯出：/export 或 /匯出
    if text.lower() in ["/export", "/匯出", "/報告", "/結案報告", "export", "匯出"]:
        tasks = list_tasks(target_group)
        free_members, all_members, _, _ = get_unassigned_members(target_group)
        
        claimed_tasks = [t for t in tasks if t.get("status") == "claimed"]
        pending_tasks = [t for t in tasks if t.get("status") == "pending"]
        
        lines = [
            "【組長保險・小組期末分工成果報告】\n",
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
            
        lines.append("\n本紀錄由組長保險自動存證，可用於期末互評與成果報告依據。")
        return [TextMessage(text="\n".join(lines), quick_reply=get_main_quick_reply())]

    # 10. 手動新增成員名單：/member 新增 或 /成員 新增 [名字1] [名字2]...
    member_add_prefixes = (
        "/member 新增", "/member add",
        "/成員 新增", "/成員 add",
        "/組員 新增", "/名單 新增",
        "member add", "成員 新增"
    )
    matched_member_add = None
    for pfx in member_add_prefixes:
        if text.startswith(pfx):
            matched_member_add = pfx
            break

    if matched_member_add:
        names_str = text[len(matched_member_add):].strip()
        if not names_str:
            return [TextMessage(
                text="指令格式：\n• /member 新增 [組員1] [組員2] ...\n• /成員 新增 [組員1] [組員2] ...\n\n例如：\n/成員 新增 小明 小華 阿美\n\n（適合直接將未發言的組員加入抽籤池）",
                quick_reply=get_main_quick_reply()
            )]
        
        names = [n.strip() for n in re.split(r"[,，\s]+", names_str) if n.strip()]
        added = []
        for name in names:
            if add_manual_member(target_group, name):
                added.append(name)
                
        if added:
            return [TextMessage(text=f"已將 {len(added)} 位成員加入群組抽籤名冊：\n{', '.join(added)}\n\n未指派任務時將優先納入隨機抽籤池。", quick_reply=get_main_quick_reply())]
        else:
            return [TextMessage(text="未能成功解析成員名稱，請確認輸入格式。", quick_reply=get_main_quick_reply())]

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
            return [TextMessage(text="目前群組名冊尚無成員。\n組員可在群內發言、傳貼圖，或由組長輸入：\n/成員 新增 小明 小華 阿美", quick_reply=get_main_quick_reply())]
            
        task_map = {}
        for t in all_tasks:
            if t.get("status") == "claimed" and t.get("assignee_id"):
                task_map[t["assignee_id"]] = t.get("title", "")

    # 11 (cont). 組合名冊顯示文字
        lines = ["【小組成員與任務現況】"]
        for m in all_members:
            uid = m.get("user_id", "")
            uname = m.get("user_name", "組員")
            if uid in task_map:
                lines.append(f"• {uname}：負責「{task_map[uid]}」")
            else:
                lines.append(f"• {uname}：尚未分配任務（抽籤候選）")
                
        lines.append("\n若有名單遺漏，可由組長使用：\n/member 新增 或 /成員 新增 [名字1] [名字2]")
        return [TextMessage(text="\n".join(lines), quick_reply=get_main_quick_reply())]

    # 12. 成員手動簽到：/checkin、/簽到 或 /報到
    if text.lower() in ["/checkin", "/簽到", "/報到", "checkin", "簽到", "報到", "+1"]:
        return [TextMessage(text=f"「{user_name}」簽到成功！已將您登記至小組名冊。", quick_reply=get_main_quick_reply())]

    # 非指令，回傳 None
    return None


