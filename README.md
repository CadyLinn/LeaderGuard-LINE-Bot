# LeaderGuard 組長保險 · LINE Bot

> **你不用當壞人，讓 AI 當法官。**
> 分工、催進度、抽籤、會議記錄都交給機器人，期末互評有憑有據。

## Demo 影片

<p align="center">
  <a href="https://www.youtube.com/shorts/QmC5gaNn8JA">
    <img src="https://img.youtube.com/vi/QmC5gaNn8JA/maxresdefault.jpg" alt="LeaderGuard Demo 影片" width="360">
  </a>
  <br>
  <a href="https://www.youtube.com/shorts/QmC5gaNn8JA">點此觀看 Demo（YouTube Shorts）</a>
</p>

LeaderGuard 是專為大專院校小組報告設計的 LINE 群組機器人。組長最常遇到三種困擾：催進度得罪人、訊息發出去全體已讀不回、期末有人搭便車卻拿不出證據。LeaderGuard 把這些「當壞人」的工作交給系統處理，並把每一次分工與認領都記錄下來。

---

## 功能總覽

| 功能 | 說明 | 主要指令 |
| --- | --- | --- |
| 任務管理 | 新增、列出、刪除群組任務，自動編號（T001、T002…） | `/任務 新增 <標題> <說明>`、`/任務`、`/刪除 <編號>` |
| 常用分工範本 | 一鍵建立報告常見分工（簡報、書面、資料蒐集…），已存在的自動略過 | `/範本`、`/一鍵建立` |
| 認領任務 | 成員主動認領，記錄認領人與時間 | `/認領 T001`、`我負責 T001` |
| 死鬥輪盤 | 從尚未分到工作的成員中隨機抽出一位，指派一項待認領任務，人情壓力轉嫁給系統 | `/抽籤`、`/抽籤 小明 小華 小美` |
| 組員名冊 | 發言、傳貼圖、入群都會自動登記；也能手動設定名單 | `/組員 小明, 小華`、`/組員`、`/組員 清空`、`/簽到` |
| AI 催繳提醒 | 依待認領任務產生提醒卡片，可切換友善版或正式版（含「教授」「期限」等字眼時） | `/催繳`、`/提醒 正式` |
| 進度與結案報告 | 查看完成狀態；匯出每位成員負責的任務與尚未分工的人 | `/進度`、`/匯出` |
| AI 會議記錄（PRO） | 開會期間自動收錄群組對話，結束後由 Gemini 整理摘要、決議與待辦事項 | `/開始會議`、`/結束會議` |
| 升級方案 | 顯示方案卡片並一鍵開通 PRO | `/升級方案`、`/解鎖會議` |

其他輔助指令：`/選單`（主選單）、`/指令說明`、`/使用手冊`、`/加入群組`（邀請機器人進群的教學）。
大部分指令都接受多種寫法（中英文、有無斜線、全形斜線「／」），細節見 `app/services/command_handler.py`。

> **PRO 權限**：尚未串接金流，PRO 只開放給 `PRO_GROUP_IDS` 中的群組，或由 `PRO_ADMIN_USER_IDS` 中的管理員在群組內輸入 `/解鎖會議` 開通（存在記憶體，重啟後需重新解鎖）。其他人使用 PRO 指令只會看到方案說明。

---

## 技術架構

```text
LINE 群組 / 私聊
      │  Webhook（簽章驗證）
      ▼
FastAPI（app/main.py）
  ├─ routes/webhook.py          事件分派：訊息、貼圖、入群、加好友、Postback
  ├─ services/command_handler.py 指令解析 → 回傳 Flex / 文字訊息
  ├─ services/firebase_service.py 群組、成員、任務存取（Firestore ⇄ 本地 JSON）
  ├─ services/meeting_service.py  會議收錄與 Gemini 摘要
  └─ utils/flex_templates.py      所有 Flex Message 卡片樣式
```

- **後端**：Python 3.11、FastAPI、Uvicorn
- **LINE**：`line-bot-sdk` v3（Messaging API、Flex Message、Rich Menu）
- **資料庫**：Firebase Firestore；未設定憑證或連線逾時（1 秒）時，自動改用 `data/local_storage.json`
- **AI**：Google Gemini（`google-generativeai`）；未設定 API Key 時改用規則式摘要
- **圖片**：`assets/` 由 FastAPI 以 `/assets` 提供靜態檔，供 Flex 卡片引用

### 目錄結構

```text
LeaderGuard-LINE-Bot/
├─ app/
│  ├─ main.py                 # FastAPI 入口、靜態資源、健康檢查
│  ├─ routes/webhook.py       # LINE Webhook 事件處理
│  ├─ services/
│  │  ├─ command_handler.py   # 指令路由
│  │  ├─ firebase_service.py  # 資料存取（含本地備援）
│  │  └─ meeting_service.py   # AI 會議記錄、PRO 解鎖
│  └─ utils/flex_templates.py # Flex Message 樣板
├─ assets/                    # Flex 卡片與 Rich Menu 圖片、字型
├─ data/local_storage.json    # 本地備援資料
├─ scripts/
│  ├─ setup_rich_menu.py      # 產生並上傳 Rich Menu
│  └─ generate_*.py           # 簡報 / 講稿產生工具
├─ presentation/              # 競賽簡報、講稿、展示頁
├─ Procfile                   # 雲端部署啟動指令
└─ requirements.txt
```

---

## 快速開始

### 1. 準備

- Python 3.11（見 `.python-version`）
- [LINE Developers](https://developers.line.biz/) 建立 Messaging API Channel，取得 **Channel Secret** 與 **Channel Access Token**
- （選用）Firebase 專案與服務帳戶金鑰
- （選用）Google Gemini API Key

### 2. 安裝

```bash
git clone https://github.com/CadyLinn/LeaderGuard-LINE-Bot.git
cd LeaderGuard-LINE-Bot
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### 3. 設定環境變數（`.env`）

| 變數 | 必填 | 說明 |
| --- | --- | --- |
| `LINE_CHANNEL_SECRET` | 是 | LINE Channel Secret |
| `LINE_CHANNEL_ACCESS_TOKEN` | 是 | LINE Channel Access Token |
| `GEMINI_API_KEY` | | 會議 AI 摘要；未填則用規則式摘要 |
| `FIREBASE_CREDENTIALS_PATH` | | 服務帳戶金鑰路徑，預設 `serviceAccountKey.json` |
| `FIREBASE_CREDENTIALS_JSON` | | 直接放金鑰 JSON 字串（雲端部署較方便，優先於路徑） |
| `PRO_ADMIN_USER_IDS` | | 可用 `/解鎖會議` 開通 PRO 的管理員 LINE userId，逗號分隔 |
| `PRO_GROUP_IDS` | | 永久開通 PRO 的群組 ID，逗號分隔 |
| `ADMIN_API_TOKEN` | | `/api/logs` 的存取權杖；留空則該端點完全關閉 |

> `.env` 與 `serviceAccountKey.json` 已列入 `.gitignore`，請勿提交到版本控制。

### 4. 啟動

```bash
uvicorn app.main:app --reload --port 8000
```

本機測試可用 [ngrok](https://ngrok.com/) 等工具建立 HTTPS 通道，然後在 LINE Developers 後台將 Webhook URL 設為：

```
https://<你的網域>/webhook
```

（`/webhook/`、`/callback` 也可以用）並開啟 **Use webhook**、允許機器人加入群組。

### 5. 設定 Rich Menu（選用）

```bash
python scripts/setup_rich_menu.py
```

會產生三格圖文選單：使用手冊、常用指令、升級方案。

---

## 部署

專案附有 `Procfile`，可直接部署到 Render、Railway、Heroku 等支援 Python 的平台：

```text
web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

在平台上設定上述環境變數即可，Firebase 金鑰建議使用 `FIREBASE_CREDENTIALS_JSON`。
注意：本地 JSON 備援模式在多數雲端平台重啟後會遺失資料，正式使用請接上 Firestore。

### 診斷用端點

| 路徑 | 用途 |
| --- | --- |
| `GET /` | 服務狀態 |
| `GET /health` | 健康檢查 |
| `GET /version` | 目前版本與更新說明 |
| `GET /api/logs` | 最近 50 筆 Webhook 收發紀錄（記憶體），需權杖 |

`/api/logs` 含使用者 ID 與訊息內容，必須帶權杖才能讀取（也可用來查自己的 LINE userId / 群組 ID）：

```bash
curl -H "Authorization: Bearer $ADMIN_API_TOKEN" https://<你的網域>/api/logs
```

> 本地備援資料 `data/local_storage.json` 含真實群組與成員資料，已列入 `.gitignore`，不會進版本控制。

---

## 方案規劃

| 方案 | 內容 |
| --- | --- |
| 免費版 | 任務建立與認領、分工範本、死鬥輪盤、組員名冊、進度查詢、AI 催繳 |
| PRO 會議記錄方案 | `/開始會議`、`/結束會議` AI 統整重點與待辦、分工與成果存證報告（`/匯出`）、多專案與多群組管理 |

---

## 開發路線圖

以下為原始企劃中、尚未實作的功能：

- [ ] **沉寂偵測**：群組超過設定時間沒有人發言，自動推送 meme 風格 Flex 卡片（「重大集體失蹤案」）
- [ ] **逾時自動抽籤**：任務超時無人認領時自動觸發死鬥輪盤（目前需手動 `/抽籤`）
- [ ] **LIFF 查閱追蹤**：透過 LIFF 任務頁記錄誰打開過任務、何時打開
- [ ] **期中 / 期末貢獻度 PDF 報告**：統計準時完成率、回覆延遲、主動認領次數，產出可附在互評表的 PDF
- [ ] **金流與方案權限**：串接付款，依方案限制功能
- [ ] **會議與 PRO 狀態持久化**：目前存在記憶體，伺服器重啟後會清空

---

## 授權

本專案為競賽專題作品。
