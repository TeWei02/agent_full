```markdown
# Agent Full — 全自動化 AI Agent 系統

![GitHub repo size](https://img.shields.io/github/repo-size/your-username/agent_full)
![GitHub license](https://img.shields.io/github/license/your-username/agent_full)
![GitHub last commit](https://img.shields.io/github/last-commit/your-username/agent_full)
![GitHub stars](https://img.shields.io/github/stars/your-username/agent_full?style=social)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen)

**Agent Full** 是一套專為內容創作者與知識工作者設計的全自動化 AI Agent 系統。  
它能夠根據排程自動產出高品質的技術文章與商業分析內容，並直接整合至您的發布流程。

---

## Features

- 🤖 **全自動化排程** — 設定時間週期，系統自動執行產出任務
- 📝 **多領域內容生成** — 支援技術（tech）與商業（biz）兩大類別
- 🧠 **AI 驅動分析** — 基於最新語言模型，產出深度且具洞察力的文章
- 🗂️ **結構化輸出** — 檔案自動命名為 `YYYYMMDD_類別_標題.md` 格式
- 🔌 **易於擴展** — 可透過 Plugin 架構新增內容類型或輸出目標

---

## Installation

### 前置需求

- Python 3.10 或更高版本
- Git
- 有效的 OpenAI API 金鑰（或相容 LLM 服務）

### 安裝步驟

```bash
# 1. 克隆倉庫
git clone https://github.com/your-username/agent_full.git
cd agent_full

# 2. 建立虛擬環境（建議）
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 安裝依賴套件
pip install -r requirements.txt

# 4. 設定環境變數
cp .env.example .env
# 編輯 .env 檔案，填入你的 API 金鑰與設定
```

---

## Usage

### 基本執行

啟動系統並執行一次內容產出：

```bash
python run_agent.py --mode single
```

### 排程模式

設定每日定時執行（例如每天早上 8:00）：

```bash
python run_agent.py --mode schedule --time "08:00"
```

### 自訂內容類型

僅產出技術類文章：

```bash
python run_agent.py --category tech
```

### 輸出範例

執行後，系統會自動在 `output/` 目錄下產生結構化 Markdown 檔案：

```
output/
├── tech_20260617_Linux命令行技巧：提升效率的10個組.md
└── biz_20260617_訂閱制商業模式深度解析.md
```

---

## 今日產出內容範例

| 類別 | 檔案名稱 | 主題 |
|------|----------|------|
| 🖥️ Tech | `20260617_Linux命令行技巧：提升效率的10個組.md` | Linux 命令列實用技巧 |
| 💼 Biz  | `20260617_訂閱制商業模式深度解析.md` | 訂閱制商業模式分析 |

---

## Project Structure

```
agent_full/
├── agents/             # AI Agent 核心邏輯
├── config/             # 設定檔與環境變數
├── output/             # 產出內容存放目錄
├── plugins/            # 擴充插件
├── templates/          # 提示詞模板
├── run_agent.py        # 主程式入口
├── requirements.txt    # Python 依賴
└── README.md           # 本文件
```

---

## License

本專案採用 **MIT License** — 詳細條款請參閱 [LICENSE](LICENSE) 檔案。

---

*Automated by Davin Portfolio Engine*
```