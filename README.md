# LeaderGuard

一個使用 **Python FastAPI**、部署於 **GCP** 的 LINE Bot，協助大專院校專案組長管理沉寂與任務分配。

## 目錄結構
```
leaderguard/
├─ app/
│  ├─ main.py
│  ├─ routes/
│  │   ├─ webhook.py
│  │   └─ liff.py
│  ├─ services/
│  │   ├─ line_service.py
│  │   ├─ liff_service.py
│  │   ├─ task_service.py
│  │   └─ report_service.py
│  ├─ models/
│  │   ├─ member.py
│  │   └─ task.py
│  └─ utils/
│      └─ llm_prompt.py
├─ infra/
│  ├─ Dockerfile
│  └─ docker-compose.yml
├─ db/
│  └─ schema.sql
├─ requirements.txt
└─ README.md
```

## 快速開始
1. 於 GCP 建立 Cloud Run 環境。
2. 設定環境變數 `LINE_CHANNEL_SECRET`, `LINE_CHANNEL_ACCESS_TOKEN` 與 `GEMINI_API_KEY`。
3. 部署 Docker 映像即可。

---
如需進一步實作各模組，請告知。
