import logging
from dotenv import load_dotenv
from fastapi import FastAPI

# 在引入任何內部模組前先載入 .env 變數
load_dotenv()

# 設定全域日誌格式
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("leaderguard")

from app.routes import webhook
from app.services.firebase_service import init_firebase

app = FastAPI(title="LeaderGuard LINE Bot")

# 啟動時初始化 Firebase
@app.on_event("startup")
async def startup_event():
    logger.info("LeaderGuard LINE Bot 伺服器啟動中...")
    init_firebase()

import os
from fastapi.staticfiles import StaticFiles

# 掛載靜態資源目錄（供 LINE Flex 卡片引用高品質圖檔）
if os.path.exists("assets"):
    app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# 註冊路由
app.include_router(webhook.router)

@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "LeaderGuard LINE Bot",
        "message": "智慧校園小組協作與已讀不回審判庭 API 已就緒"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "LeaderGuard LINE Bot"
    }

from app.routes.webhook import recent_webhook_logs

@app.get("/version")
def get_version():
    return {
        "version": "1.10.5",
        "build": "invite-group-card-visual-and-color-upgrade",
        "description": "升級加進群組 Flex Message 視覺配色與按鈕色彩，加入步驟精美圖解與一鍵分享功能"
    }

@app.get("/api/logs")
def get_webhook_logs():
    return {
        "total_events": len(recent_webhook_logs),
        "logs": list(reversed(recent_webhook_logs))
    }



