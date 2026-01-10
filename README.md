# Agent Full

> 一個功能完整的 AI Agent 專案，結合本地 LLM 與 RAG 技術

## ✨ 專案簡介

這是一個基於本地大語言模型的 AI Agent 系統，目標是建構一個具備檢索增強生成（RAG）能力的智能助手。專案使用 Ollama 作為本地模型推理引擎，搭配 LlamaIndex 進行向量檢索與文檔管理。

## 🎯 主要功能

- **本地 LLM 推理**：使用 Ollama 運行本地大語言模型，保護數據隱私
- **RAG 檢索增強**：整合向量資料庫，提供上下文相關的智能回答
- **Agent 工具鏈**：支援多種工具調用與任務執行能力
- **靈活架構**：模組化設計，易於擴展與客製化

## 📁 專案結構

```
agent_full/
├── agent_full/
│   └── agent_full/
│       └── data/           # 核心資料目錄
│           ├── notes.txt   # 筆記與開發記錄
│           └── project.txt # 專案規劃文件
├── data/                   # 外部資料目錄
│   ├── notes.txt          # 使用者筆記
│   └── project.txt        # 專案資訊
├── .github/               # GitHub 配置
│   └── instructions/      # AI 指令配置
│       └── codacy.instructions.md
├── .gitignore            # Git 忽略規則
├── .env.example          # 環境變數範本
└── README.md             # 專案說明文件
```

## 🚀 快速開始

### 環境需求

- Python 3.8+
- Ollama（本地 LLM 運行環境）
- Node.js 16+（選用，用於前端介面）

### 安裝步驟

1. **Clone 專案**
   ```bash
   git clone https://github.com/TeWei02/agent_full.git
   cd agent_full
   ```

2. **安裝 Ollama**
   ```bash
   # macOS
   brew install ollama
   
   # 或從官網下載：https://ollama.ai
   ```

3. **下載模型**
   ```bash
   ollama pull llama2
   # 或其他模型：mistral, codellama, mixtral 等
   ```

4. **設定環境變數**
   ```bash
   cp .env.example .env
   # 編輯 .env 填入必要配置
   ```

5. **安裝依賴**
   ```bash
   pip install -r requirements.txt
   # 或
   npm install
   ```

## 💡 使用方式

### 基本使用

```python
from agent import AgentFull

# 初始化 Agent
agent = AgentFull(model="llama2")

# 執行查詢
response = agent.query("請幫我總結 data/project.txt 的內容")
print(response)
```

### RAG 檢索

```python
# 載入文檔
agent.load_documents("./data")

# 進行 RAG 查詢
answer = agent.rag_query("專案的主要目標是什麼？")
print(answer)
```

## 🛠️ 技術棧

- **LLM 框架**：Ollama
- **向量檢索**：LlamaIndex / ChromaDB
- **語言**：Python 3.x
- **資料處理**：Pandas, NumPy
- **API 框架**：FastAPI / Flask（規劃中）

## 📊 開發進度

- [x] 專案架構設計
- [x] 基礎資料結構建立
- [ ] Ollama 本地模型整合
- [ ] LlamaIndex 向量資料庫實作
- [ ] Agent 工具鏈開發
- [ ] Web API 介面
- [ ] 前端互動界面

## 📝 開發筆記

詳細的開發記錄請參考：
- [data/notes.txt](data/notes.txt) - 日常開發筆記
- [data/project.txt](data/project.txt) - 專案規劃與目標

## 🤝 貢獻指南

歡迎提交 Issue 或 Pull Request！

1. Fork 本專案
2. 建立特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交變更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

## 👨‍💻 作者

**TeWei**
- 計算機科學系學生 @ STUST
- GitHub: [@TeWei02](https://github.com/TeWei02)

## 📄 授權

