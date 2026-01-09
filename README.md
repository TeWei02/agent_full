# 🧠 AI Computer

> **跨語言智慧系統** - 完全免費開源的 AI 助手  
> 由 STUST 計算機科學系學生開發

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Stars](https://img.shields.io/github/stars/yourusername/ai-computer.svg)](https://github.com/yourusername/ai-computer/stargazers)

## ✨ 專案亮點

- 🤖 **本地 AI** - 使用 Ollama，完全免費，無需 API 密鑰
- 🔧 **多語言整合** - Python、Go、Rust、C++ 跨語言協作
- 💾 **長期記憶** - 智慧學習系統，記住用戶偏好
- 🌐 **現代化 UI** - React + TypeScript Web 界面
- 🚀 **完全開源** - MIT 授權，歡迎貢獻

## 🎯 專案動機

作為 Southern Taiwan University of Science and Technology 的計算機科學學生，我開發此專案來：

1. **展示系統設計能力** - 完整的 AI Agent 架構
2. **實踐多語言開發** - 整合 7+ 種程式語言
3. **探索 AI 技術** - 本地 LLM 部署與應用
4. **建立開源作品** - 回饋社群，幫助他人學習

## 🚀 快速開始

### 前置需求

- Python 3.8+
- [Ollama](https://ollama.com) (免費的本地 LLM 運行工具)

### 安裝步驟

```bash
# 1. 安裝 Ollama（免費）
curl -fsSL https://ollama.com/install.sh | sh

# 2. 下載推薦模型（免費，約 2GB）
ollama pull llama3.2

# 3. 克隆專案
git clone https://github.com/yourusername/ai-computer.git
cd ai-computer

# 4. 安裝 Python 依賴（全部免費）
pip install -r requirements-free.txt

# 5. 啟動系統
python3 main.py
就這樣！無需 API 密鑰，完全免費！ ✅

📖 使用範例
CLI 模式
bash
$ python3 main.py

AI > 幫我分析這段 Python 代碼

🧠 思考中...
📋 制定計劃...
⚙️  執行中...

✅ 分析完成！
Web UI
bash
# 啟動 Web 界面
cd web/frontend
npm install
npm run dev

# 訪問 http://localhost:3000
🏗️ 系統架構
text
┌─────────────────────────────────────────┐
│          Web UI (React)                 │
├─────────────────────────────────────────┤
│       API Server (FastAPI)              │
├─────────────────────────────────────────┤
│         AI Core (Python)                │
│  ┌────────┬─────────┬──────────┐       │
│  │ Brain  │ Memory  │ Executor │       │
│  │(Ollama)│(SQLite) │          │       │
│  └────────┴─────────┴──────────┘       │
├─────────────────────────────────────────┤
│           Tools Layer                   │
│   Python│Go│Rust│C++│R│Julia           │
└─────────────────────────────────────────┘
🛠️ 技術棧
核心層
Python - AI 大腦、協調器

Go - 高併發服務

Rust - 安全關鍵組件

C++ - 系統級驅動

AI 層
Ollama - 本地 LLM 運行時（免費）

Llama 3.2 - Meta 開源模型（免費）

ChromaDB - 向量資料庫（免費）

Web 層
React + TypeScript - 前端

FastAPI - 後端 API

WebSocket - 實時通訊

📊 功能展示
1. 自然語言任務
python
# 用戶輸入
"幫我創建一個待辦事項清單"

# AI 自動：
✓ 理解任務
✓ 制定計劃
✓ 調用工具
✓ 執行並反饋
2. 程式碼分析
python
# 分析任何程式碼
brain.analyze_code(code, language="python")

# 返回：
- 功能說明
- 潛在問題
- 改進建議
3. 多語言工具調用
bash
# 自動選擇最適合的語言執行任務
- Python → 數據處理
- Go → 網路服務
- Rust → 加密操作
- C++ → 系統控制
🎓 學習成果
通過此專案，我掌握了：

✅ 系統架構設計 - 完整的 Agent 架構

✅ 多語言整合 - FFI、IPC、API 設計

✅ AI 應用開發 - LLM 集成與優化

✅ DevOps - Docker、CI/CD、監控

✅ 開源協作 - Git workflow、文檔撰寫

📈 專案統計
代碼行數: ~10,000+ 行

支援語言: 7+ 種

工具數量: 30+ 個

開發時間: 3 個月

測試覆蓋: 85%+

🔮 未來計劃
 支援更多本地模型（Mistral、Qwen）

 加入語音交互功能

 移動端 App（React Native）

 插件系統（用戶自定義工具）

 多用戶支持

🤝 貢獻
歡迎貢獻！請查看 CONTRIBUTING.md

貢獻者
感謝所有貢獻者！

<!-- 這裡會自動生成貢獻者列表 -->
📄 授權
MIT License - 詳見 LICENSE

👨‍💻 關於作者
TeWei
計算機科學系學生 @ Southern Taiwan University of Science and Technology

🎓 專業: Computer Science

💡 興趣: AI、Systems Programming、Open Source

🌱 正在學習: Advanced AI Agents、Distributed Systems

📫 聯絡方式
Email: your.email@example.com

LinkedIn: linkedin.com/in/yourprofile

GitHub: @yourusername

Portfolio: yourwebsite.com

🏆 其他專案
專案1 - 簡短描述

專案2 - 簡短描述

🙏 致謝
Ollama - 免費的本地 LLM 工具

Meta AI - Llama 3.2 開源模型

STUST - 我的母校

⭐ Star History
如果這個專案對你有幫助，請給個 Star！
Built with ❤️ by TeWei
Let's make AI accessible to everyone!
