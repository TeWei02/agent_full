# Agent Full

[![Python](https://img.shields.io/badge/Python-3.10--3.12-%233776AB?logo=python)](https://www.python.org/)
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-%232088FF?logo=githubactions)](https://github.com/features/actions)
[![Status](https://img.shields.io/badge/Status-Experimental-orange)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

本地語言模型 Agent 的實驗與筆記倉庫，記錄在 macOS 上以開源模型與檢索增強技術（RAG）搭建個人助理系統的過程。

## 狀態

> **實驗中**：此為個人實驗筆記，記錄環境建置、依賴選用與架構規劃，尚未形成完整可交付的應用程式。

## 內容

| 項目 | 說明 |
|------|------|
| 實驗筆記 | `data/notes.txt` — 環境建置與實作紀錄 |
| 專案規劃 | `data/project.txt` — 本地檢索問答系統的目標與架構構想 |
| 依賴清單 | `requirements.txt` — 雲端 API（Groq / OpenAI）與本地模型（Ollama / LlamaIndex） |
| 持續整合 | `.github/workflows/` — Python 3.10–3.12 的 flake8 + pytest CI 流程 |
| 設定範本 | `.env.example` — API 金鑰環境變數範本 |

## 技術方向

- 語言模型推論：Groq / OpenAI API，以及 Ollama 本地模型
- 語意檢索與知識庫問答：LlamaIndex 向量檢索
- 環境管理：python-dotenv、Conda / pip

## 專案結構

```
agent_full/
├── .env.example            # 環境變數範本
├── requirements.txt        # Python 依賴
├── data/
│   ├── notes.txt           # 實驗筆記
│   └── project.txt         # 專案規劃
└── .github/workflows/      # CI 設定
```

## License

MIT © [Te-Wei Ko](https://github.com/TeWei02)
