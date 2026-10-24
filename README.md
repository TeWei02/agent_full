# Agent Full

**Language:** [![中文](https://img.shields.io/badge/%E4%B8%AD%E6%96%87-%E4%B8%AD%E6%96%87%E7%89%88-blue?style=flat-square)](README.md) [![English](https://img.shields.io/badge/English-English-blue?style=flat-square)](README.en.md)

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
├── docs/
│   ├── modern-agent/       # 框架層設計（原 Modern_agent，已歸檔）
│   └── universaal-agent/   # 通用型架構（原 UNIVERSAAL_AGENT，已歸檔）
├── experiments/            # 概念驗證與實驗（預留）
└── .github/workflows/      # CI 設定
```

## 規劃倉庫已歸檔，內容合併於此

Agent 研究系列的規劃倉庫 **Modern_agent**（框架層設計：工具使用、情境記憶管理、多模型整合）與 **UNIVERSAAL_AGENT**（通用型架構：跨領域任務規劃、工具整合與知識管理）已於 2026-10-24 歸檔（archived），其規劃文檔已合併至本倉庫 `docs/` 目錄並保留來源標註。

| 原倉庫 | 定位 | 合併位置 |
| --- | --- | --- |
| Modern_agent（已歸檔） | 框架層設計：工具使用、情境記憶管理、多模型整合 | [docs/modern-agent/](docs/modern-agent/) |
| UNIVERSAAL_AGENT（已歸檔） | 通用型架構：跨領域任務規劃、工具整合與知識管理 | [docs/universaal-agent/](docs/universaal-agent/) |
| agent_full（本倉庫） | 落地實驗：macOS 本地模型與 RAG 的實作紀錄 | — |

本倉庫現作為 Agent 研究系列的單一主倉庫，涵蓋落地實驗、架構規劃與框架設計三個面向。

## License

MIT © [Te-Wei Ko](https://github.com/TeWei02)
