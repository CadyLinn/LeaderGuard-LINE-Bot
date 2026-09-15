import os
import logging
import random
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore

logger = logging.getLogger("leaderguard.firebase")

db = None

# 本機/離線測試用的記憶體暫存 (在 serviceAccountKey.json 尚未備妥時自動無縫墊檔)
_memory_tasks = []
_memory_groups = {}
_memory_members = {}

def init_firebase():
    """初始化 Firebase Admin SDK（具備連線檢驗與防卡死機制）"""
    global db
    if db is not None:
        return db

    cred_json = os.getenv("FIREBASE_CREDENTIALS_JSON")
    cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH", "serviceAccountKey.json")
    
    cred = None
    if cred_json:
        try:
            import json
            cred_dict = json.loads(cred_json)
            cred = credentials.Certificate(cred_dict)
            logger.info("使用環境變數 FIREBASE_CREDENTIALS_JSON 憑證載入 Firebase")
        except Exception as e:
            logger.error(f"解析 FIREBASE_CREDENTIALS_JSON 失敗: {e}")
    elif os.path.exists(cred_path):
        try:
            cred = credentials.Certificate(cred_path)
            logger.info(f"使用實體金鑰檔案 [{cred_path}] 載入 Firebase")
        except Exception as e:
            logger.error(f"載入憑證檔案失敗: {e}")

    if cred:
        try:
            if not firebase_admin._apps:
                firebase_admin.initialize_app(cred)
            test_client = firestore.client()
            # 進行 2 秒超時快速健康檢查，確認 Firestore API 是否已在 Firebase 後台啟用
            try:
                test_client.collection("_health_check").limit(1).get(timeout=2)
                db = test_client
                logger.info("✅ Firebase Firestore 成功連線並通過驗證！")
            except Exception as conn_err:
                logger.warning(
                    f"⚠️ Firebase 專案尚未在 Firebase Console 啟用 Firestore Database！"
                    f"錯誤訊息: {conn_err}。\n"
                    "👉 系統已自動切換為「本地記憶體高速模式」，確保 LINE Bot 訊息絕不卡頓或逾時！"
                )
                db = None
        except Exception as e:
            logger.error(f"Firebase 初始化失敗: {e}")
            db = None
    else:
        logger.warning(f"尚未配置 Firebase 憑證，啟用「本地記憶體模式」確保功能順暢運作！")
        db = None
        
    return db

def get_db():
    global db
    if db is None:
        init_firebase()
    return db

def update_group_activity(group_id: str, last_message_text: str = None, user_id: str = None):
    """相容性別名：更新群組活動紀錄"""
    return record_member_activity(group_id, user_id or "unknown", "組員", last_message_text)

# --- 成員與群組活動管理 ---

def record_member_activity(group_id: str, user_id: str, user_name: str = None, message_text: str = None):
    """記錄群組與成員發言（作為死鬥輪盤抽籤名單與沉寂追蹤）"""
    database = get_db()
    
    # 紀錄群組成員名冊（記憶體）
    if group_id not in _memory_members:
        _memory_members[group_id] = {}
    _memory_members[group_id][user_id] = {
        "user_name": user_name or "組員",
        "last_seen": datetime.now()
    }
    
    _memory_groups[group_id] = {
        "last_active_at": datetime.now(),
        "last_message": message_text,
        "last_sender_id": user_id
    }

    if not database:
        return

    try:
        group_ref = database.collection("groups").document(group_id)
        group_ref.set({
            "last_active_at": firestore.SERVER_TIMESTAMP,
            "last_message": message_text,
            "last_sender_id": user_id,
            "updated_at": firestore.SERVER_TIMESTAMP
        }, merge=True)

        member_ref = database.collection("groups").document(group_id).collection("members").document(user_id)
        member_ref.set({
            "user_name": user_name or "組員",
            "last_seen": firestore.SERVER_TIMESTAMP
        }, merge=True)
    except Exception as e:
        logger.error(f"Firestore 更新成員紀錄失敗: {e}")

def get_group_members(group_id: str):
    """取得該群組已知成員名單（包含發過言的組員、點選過的組員與手動加入的名冊）"""
    database = get_db()
    members = []
    
    if database:
        try:
            docs = database.collection("groups").document(group_id).collection("members").stream()
            for doc in docs:
                m = doc.to_dict()
                m["user_id"] = doc.id
                members.append(m)
        except Exception as e:
            logger.error(f"取得群組成員失敗: {e}")
            
    if not members and group_id in _memory_members:
        for uid, data in _memory_members[group_id].items():
            members.append({"user_id": uid, "user_name": data["user_name"]})
    elif group_id in _memory_members:
        known_ids = {m["user_id"] for m in members}
        for uid, data in _memory_members[group_id].items():
            if uid not in known_ids:
                members.append({"user_id": uid, "user_name": data["user_name"]})

    return members

def add_manual_member(group_id: str, member_name: str):
    """手動將成員名稱加入該群組的抽籤池（針對完全不發言的幽靈組員）"""
    database = get_db()
    member_name = member_name.strip()
    if not member_name:
        return False
        
    user_id = f"manual_{member_name}"
    if group_id not in _memory_members:
        _memory_members[group_id] = {}
    _memory_members[group_id][user_id] = {
        "user_name": member_name,
        "last_seen": datetime.now(),
        "is_manual": True
    }
    
    if database:
        try:
            member_ref = database.collection("groups").document(group_id).collection("members").document(user_id)
            member_ref.set({
                "user_name": member_name,
                "last_seen": firestore.SERVER_TIMESTAMP,
                "is_manual": True
            }, merge=True)
        except Exception as e:
            logger.error(f"手動新增成員失敗: {e}")
            
    return True

# --- 任務管理 ---

def record_task(group_id: str, title: str, description: str, creator_id: str):
    """建立新任務"""
    database = get_db()
    task_id = f"T{len(_memory_tasks) + 1:03d}"
    
    task_dict = {
        "id": task_id,
        "group_id": group_id,
        "title": title,
        "description": description,
        "creator_id": creator_id,
        "status": "pending",  # pending(待認領), claimed(已認領), completed(已完成)
        "assignee_id": None,
        "assignee_name": None,
        "created_at": datetime.now().strftime("%m/%d %H:%M")
    }
    _memory_tasks.append(task_dict)

    if database:
        try:
            doc_ref = database.collection("tasks").document(task_id)
            doc_ref.set({
                "group_id": group_id,
                "title": title,
                "description": description,
                "creator_id": creator_id,
                "status": "pending",
                "assignee_id": None,
                "assignee_name": None,
                "created_at": firestore.SERVER_TIMESTAMP
            })
        except Exception as e:
            logger.error(f"Firestore 儲存任務失敗: {e}")

    return task_id

def list_tasks(group_id: str, status: str = None):
    """取得群組任務清單"""
    database = get_db()
    tasks = []

    if database:
        try:
            query = database.collection("tasks").where("group_id", "==", group_id)
            if status:
                query = query.where("status", "==", status)
            for doc in query.stream():
                t = doc.to_dict()
                t["id"] = doc.id
                tasks.append(t)
        except Exception as e:
            logger.error(f"查詢任務失敗: {e}")

    if not tasks:
        tasks = [
            t for t in _memory_tasks 
            if t["group_id"] == group_id and (status is None or t["status"] == status)
        ]

    return tasks

def claim_task(task_id: str, user_id: str, user_name: str = None):
    """成員認領任務"""
    database = get_db()
    success = False
    task_title = ""

    for t in _memory_tasks:
        if t["id"].lower() == task_id.lower() and t["status"] == "pending":
            t["status"] = "claimed"
            t["assignee_id"] = user_id
            t["assignee_name"] = user_name or "組員"
            task_title = t["title"]
            success = True
            break

    if database:
        try:
            doc_ref = database.collection("tasks").document(task_id)
            doc = doc_ref.get()
            if doc.exists and doc.to_dict().get("status") == "pending":
                task_title = doc.to_dict().get("title", "")
                doc_ref.update({
                    "status": "claimed",
                    "assignee_id": user_id,
                    "assignee_name": user_name or "組員",
                    "claimed_at": firestore.SERVER_TIMESTAMP
                })
                success = True
        except Exception as e:
            logger.error(f"認領任務失敗: {e}")

    return success, task_title

def assign_roulette_task(group_id: str, chosen_user_id: str, chosen_user_name: str):
    """死鬥輪盤隨機將待認領任務指派給指定成員"""
    pending_tasks = list_tasks(group_id, status="pending")
    if not pending_tasks:
        return None, None
        
    target_task = random.choice(pending_tasks)
    task_id = target_task["id"]
    
    # 執行指派
    database = get_db()
    for t in _memory_tasks:
        if t["id"] == task_id:
            t["status"] = "claimed"
            t["assignee_id"] = chosen_user_id
            t["assignee_name"] = chosen_user_name
            break
            
    if database:
        try:
            database.collection("tasks").document(task_id).update({
                "status": "claimed",
                "assignee_id": chosen_user_id,
                "assignee_name": chosen_user_name,
                "claimed_at": firestore.SERVER_TIMESTAMP,
                "forced_assignment": True
            })
        except Exception as e:
            logger.error(f"輪盤指派任務更新失敗: {e}")
            
    return task_id, target_task["title"]

def get_unassigned_members(group_id: str):
    """
    取得群組中目前尚未被分配任何任務的成員名單
    回傳：
        free_members: 尚未有任務的成員清單
        all_members: 該群組所有已知成員清單
        all_tasks: 該群組所有任務
        pending_tasks: 該群組待認領任務
    """
    all_members = get_group_members(group_id)
    all_tasks = list_tasks(group_id)
    pending_tasks = [t for t in all_tasks if t.get("status") == "pending"]
    
    assigned_user_ids = {
        t["assignee_id"] for t in all_tasks 
        if t.get("status") == "claimed" and t.get("assignee_id")
    }
    
    free_members = [m for m in all_members if m["user_id"] not in assigned_user_ids]
    return free_members, all_members, all_tasks, pending_tasks
