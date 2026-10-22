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
import secrets
from fastapi import Header, HTTPException
from fastapi.staticfiles import StaticFiles

# 掛載靜態資源目錄（供 LINE Flex 卡片引用高品質圖檔）
if os.path.exists("assets"):
    app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# 註冊路由（同時支援 /webhook、/callback 及其尾隨斜線路徑，防止 LINE Webhook 307 或 404）
app.include_router(webhook.router)
app.add_api_route("/webhook/", webhook.line_webhook, methods=["POST"])
app.add_api_route("/callback", webhook.line_webhook, methods=["POST"])
app.add_api_route("/callback/", webhook.line_webhook, methods=["POST"])

@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "LeaderGuard LINE Bot",
        "message": "小組專案協作管理助手 API 已就緒"
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
        "version": "1.10.21",
        "build": "pro-ai-meeting-minutes",
        "description": "PRO 會議記錄統整功能上線（/開始會議, /結束會議, /解鎖會議），整合 Gemini AI 智能提取會議決議與待辦事項"
    }

ADMIN_API_TOKEN = os.getenv("ADMIN_API_TOKEN", "")

@app.get("/api/logs")
def get_webhook_logs(authorization: str = Header(None)):
    # 需帶 Authorization: Bearer <ADMIN_API_TOKEN>；未設定 token 時一律拒絕
    expected = f"Bearer {ADMIN_API_TOKEN}"
    if not ADMIN_API_TOKEN or not authorization or not secrets.compare_digest(authorization.encode(), expected.encode()):
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {
        "total_events": len(recent_webhook_logs),
        "logs": list(reversed(recent_webhook_logs))
    }



