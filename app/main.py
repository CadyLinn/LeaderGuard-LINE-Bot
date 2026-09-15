import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import webhook, liff

app = FastAPI(title="LeaderGuard LINE Bot", version="0.1.0")

# Allow CORS for LIFF front‑end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(webhook.router, prefix="/webhook", tags=["webhook"])
app.include_router(liff.router, prefix="/liff", tags=["liff"])

# Environment variables (LINE, Gemini)
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
