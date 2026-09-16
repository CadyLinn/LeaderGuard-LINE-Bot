import os
import logging
from dotenv import load_dotenv
from fastapi import APIRouter, Request, Header, HTTPException
from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
    StickerMessageContent,
    ImageMessageContent,
    JoinEvent,
    MemberJoinedEvent,
    FollowEvent,
    PostbackEvent
)
from app.utils.flex_templates import (
    create_help_flex,
    create_main_menu_flex,
    create_welcome_guide_flex
)

load_dotenv()

logger = logging.getLogger("leaderguard.webhook")

router = APIRouter(prefix="/webhook", tags=["Webhook"])

channel_secret = os.getenv("LINE_CHANNEL_SECRET", "")
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", "")

if not channel_secret:
    logger.error("❌ 警告：未讀取到 LINE_CHANNEL_SECRET！請確認專案根目錄下有 .env 檔案並設定 LINE_CHANNEL_SECRET。")

configuration = Configuration(access_token=channel_access_token)
handler = WebhookHandler(channel_secret)

@router.post("")
async def line_webhook(request: Request, x_line_signature: str = Header(None)):
    """接收 LINE Messaging API 的 Webhook 請求"""
    if not x_line_signature:
        logger.warning("收到未包含 X-Line-Signature 標頭的 Webhook 請求")
        raise HTTPException(status_code=400, detail="Missing X-Line-Signature header")

    body = await request.body()
    body_str = body.decode("utf-8")

    try:
        handler.handle(body_str, x_line_signature)
    except InvalidSignatureError:
        logger.error("簽章驗證失敗！請確認 LINE_CHANNEL_SECRET 是否正確。")
        raise HTTPException(status_code=400, detail="Invalid signature. Check your channel secret.")
    except Exception as e:
        logger.error(f"處理 Webhook 事件時發生未預期錯誤: {e}")
        return "ERROR"

    return "OK"

@handler.add(FollowEvent)
def handle_follow(event):
    """當使用者將官方帳號加入好友時，先傳送個人化問候語，接著傳送 4 步驟使用手冊 Flex 卡片"""
    user_id = getattr(event.source, "user_id", "unknown")
    logger.info(f"新好友加入: {user_id}")
    
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        user_name = "同學"
        try:
            profile = line_bot_api.get_profile(user_id)
            user_name = profile.display_name
        except Exception:
            pass

        account_name = "組長保險"

        greeting_text = (
            f"{user_name}您好！\n"
            f"我是{account_name}，感謝您加入好友！"
        )

        welcome_flex = create_welcome_guide_flex()
        if hasattr(welcome_flex, "quick_reply"):
            welcome_flex.quick_reply = None

        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[
                    TextMessage(text=greeting_text),
                    welcome_flex
                ]
            )
        )

@handler.add(JoinEvent)
def handle_join(event):
    """當機器人被加入群組時發送自我介紹與主選單卡片"""
    group_id = getattr(event.source, "group_id", None)
    logger.info(f"LeaderGuard 加入了新群組: {group_id}")
    
    welcome_text = (
        "嗨大家好！我是【組長保險】專案小幫手。\n"
        "這學期我會在群組協助大家輕鬆搞定報告分工：\n\n"
        "• 工作認領：清楚記錄誰負責什麼，隨時可查\n"
        "• 🎲 命運抽籤：沒人認領的工作隨機抽籤，公平省事\n"
        "• 進度存證：自動記錄完成狀態，期末互評有依據\n\n"
        "點擊下方選單即可立刻發起工作！"
    )
    
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[
                    TextMessage(text=welcome_text),
                    create_main_menu_flex()
                ]
            )
        )

from app.services.firebase_service import record_member_activity
from app.services.command_handler import handle_user_command

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    """處理群組或私聊文字訊息"""
    user_id = getattr(event.source, "user_id", "unknown")
    group_id = getattr(event.source, "group_id", None)
    user_text = event.message.text.strip()
    
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        
        # 嘗試取得使用者 LINE 暱稱
        user_name = "組員"
        try:
            if group_id:
                profile = line_bot_api.get_group_member_profile(group_id, user_id)
                user_name = profile.display_name
            elif user_id != "unknown":
                profile = line_bot_api.get_profile(user_id)
                user_name = profile.display_name
        except Exception:
            user_name = "組員"

        logger.info(f"收到訊息 [來自: {user_name}({user_id}), 群組: {group_id}]: {user_text}")

        # 記錄發言活躍時間與成員名單
        target_group = group_id or "default_group"
        record_member_activity(
            group_id=target_group,
            user_id=user_id,
            user_name=user_name,
            message_text=user_text
        )

        # 解析並處理指令
        reply_messages = handle_user_command(
            user_text=user_text,
            group_id=target_group,
            user_id=user_id,
            user_name=user_name
        )

        if reply_messages:
            # 使用者與官方帳號的 1 對 1 聊天室不顯示 quick reply（底部已有 Rich Menu 圖文選單）
            if not group_id:
                for msg in reply_messages:
                    if hasattr(msg, "quick_reply"):
                        msg.quick_reply = None
            try:
                line_bot_api.reply_message_with_http_info(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=reply_messages
                    )
                )
            except Exception as reply_err:
                logger.error(f"LINE 回覆訊息失敗: {reply_err}")
        elif not group_id:
            # 僅在「一對一私聊」且非特定指令時，直接回傳主選單 Flex 卡片（官方帳號聊天室不帶 quick reply）
            try:
                menu_flex = create_main_menu_flex()
                if hasattr(menu_flex, "quick_reply"):
                    menu_flex.quick_reply = None
                line_bot_api.reply_message_with_http_info(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[menu_flex]
                    )
                )
            except Exception as reply_err:
                logger.error(f"LINE 回覆私聊主選單失敗: {reply_err}")

@handler.add(MessageEvent, message=(StickerMessageContent, ImageMessageContent))
def handle_media_message(event):
    """處理群組內傳送貼圖或圖片的成員（即使不發文字，傳貼圖也能自動登記進抽籤池）"""
    user_id = getattr(event.source, "user_id", "unknown")
    group_id = getattr(event.source, "group_id", None)
    if not group_id or user_id == "unknown":
        return

    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        user_name = "組員"
        try:
            profile = line_bot_api.get_group_member_profile(group_id, user_id)
            user_name = profile.display_name
        except Exception:
            pass

        record_member_activity(
            group_id=group_id,
            user_id=user_id,
            user_name=user_name,
            message_text="[貼圖或多媒體]"
        )

@handler.add(MemberJoinedEvent)
def handle_member_joined(event):
    """當新成員加入群組時，自動將其收錄至小組成員名冊"""
    group_id = getattr(event.source, "group_id", None)
    if not group_id:
        return

    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        for m in getattr(event.joined, "members", []):
            user_id = getattr(m, "user_id", None)
            if user_id:
                try:
                    profile = line_bot_api.get_group_member_profile(group_id, user_id)
                    user_name = profile.display_name
                except Exception:
                    user_name = "組員"
                record_member_activity(group_id, user_id, user_name)

@handler.add(PostbackEvent)
def handle_postback(event):
    """處理按鈕 Postback 事件（如自訂新增任務鍵盤喚起）"""
    data = getattr(event.postback, "data", "")
    logger.info(f"收到 Postback 事件: {data}")
    # LINE 客戶端已透過 inputOption='openKeyboard' 自動在使用者輸入框帶入「/任務 新增 」
    # 此處靜默完成即可，無須回覆避免在聊天室洗版


