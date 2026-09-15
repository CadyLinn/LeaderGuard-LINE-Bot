# LeaderGuard LINE Bot (組長保險)

## 產品定位與核心痛點
**核心標語**：你不用當壞人，讓 AI 當法官；期中、期末算總帳，連呈堂證供都幫你準備好。

我們將打造一款 LINE Bot（組長保險），協助大專院校的專案組長解決以下問題：
- **人際壓力**：組長催進度容易得罪同儕。透過偵測群組沉寂期，自動發送幽默的 meme 風格 Flex Message 轉移焦點。
- **溝通沉寂**：訊息發出後全體已讀不回。若超時未認領任務，系統將啟動「死鬥輪盤」隨機抽籤分配任務。
- **課堂搭便車**：缺乏客觀量化數據。透過 LIFF 卡片點擊記錄成員是否已閱讀任務細節；並於**期中與期末**自動產生成員貢獻度報告（PDF），直接匯出提交作為客觀數據支撐。
- 支援免費版、付費單專案版、專業匯出版的分層收費模式。

## 專案目錄結構
```text
leaderguard/
├─ app/                     # FastAPI 或 Express 應用根目錄
│  ├─ main.py（或 index.js）
│  ├─ routes/
│  │   ├─ webhook.py            # 處理 LINE Webhook 事件
│  │   └─ liff.py               # LIFF 前端頁面相關介面
│  ├─ services/
│  │   ├─ line_service.py       # 與 LINE Messaging API 的封裝
│  │   ├─ liff_service.py       # LIFF 點擊記錄與資料上傳
│  │   ├─ task_service.py       # 任務管理、計時與抽籤分配
│  │   └─ report_service.py     # 統計、LLM 文案產生、PDF 匯出
│  ├─ models/
│  │   ├─ member.py             # 成員資訊模型
│  │   └─ task.py               # 任務資訊模型
│  └─ utils/
│      └─ llm_prompt.py         # LLM Prompt 產生工具
├─ infra/                   # Docker、CI/CD 設定
│  ├─ Dockerfile
│  └─ docker-compose.yml
├─ db/
│  ├─ migrations/              # 資料庫遷移腳本
│  └─ schema.sql               # PostgreSQL 表結構定義
├─ redis/                    # Redis 設定（可選）
├─ tests/                    # 單元測試、整合測試
├─ liff/                     # LIFF 前端（Vue 或 React）
│  ├─ src/
│  └─ public/
├─ requirements.txt（或 package.json）
└─ README.md
```

## 關鍵功能實作細節

### 1. 沉寂偵測 & Meme Flex Message
- **Webhook** 接收 `message` 事件，將每個群組的最新活動時間戳記寫入 Redis，TTL 設為 30 分鐘。
- 使用 Celery 或 APScheduler 定時檢查 Redis 中已過期的鍵。
- 超時後呼叫 Gemini 等 LLM 產生 meme 風格標題，組合 Flex Message（報紙頭條、法院傳票等），透過 LINE Messaging API 推送，公開點名「重大集體失蹤案」。

### 2. 死鬥輪盤隨機任務分配
- 在群組提供指令，將任務寫入資料庫。
- 若任務在設定的沉寂時間後仍未被認領，隨機抽取該群組活躍成員（排除已離職/未加入者），發送指派訊息，將人情仇恨轉移給系統。

### 3. LIFF 點擊追蹤 (精準埋點)
- 因 LINE API 不提供已讀者名單，任務透過 LINE LIFF 網頁卡片開啟。
- LIFF 頁面顯示任務清單，使用者點擊任務卡片後前端向後端送出 `userId` 與時間戳記。
- 後端記錄點擊日誌，若開啟清單後超過 15 分鐘未在群內認領或留言，發送提醒 Flex Message（例如：「某成員剛才已開啟清單查閱，責任感正在重啟中」）。

### 4. 期中 / 期末貢獻度報告 (呈堂證供)
- 彙總每位成員的 **任務準時完成率**、**平均回覆延遲時長**、**主動認領次數** 等指標。
- 可選擇於**期中**或**期末**進行結算，產出階段性報告。
- 呼叫 LLM 產生報告文字說明，並使用 PDF 產生套件生成結構化報表。
- 提供指令讓組長一鍵取得 PDF，可直接作為互評表附錄提交給授課教授。

### 5. Freemium 分層收費
- **免費版**：基礎任務建立、溫和版超時提醒、單一群組上限 1 個專案。
- **個人專案包**：解鎖「毒舌嘴替／嚴格教授」AI 人格包、死鬥抽籤輪盤。
- **呈堂證供專業版**：匯出完整《小組貢獻度分析 PDF 報告》、LIFF 查閱時間戳記紀錄。
- 中介軟體在請求入口檢查當前組織層級，限制高階功能。

## 後續待確認事項
1. **後端語言**：Python（FastAPI）或 Node.js（Express）？
2. **LLM 供應商**：Gemini API 是否已準備好？
3. **部署平台**：Render, Railway, 或是自行 Docker 部署？
4. **前端框架**：LIFF 選用 Vue.js 還是 React？
