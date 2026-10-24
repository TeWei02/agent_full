> **來源**：[TeWei02/Modern_agent](https://github.com/TeWei02/Modern_agent)（規劃倉庫，已歸檔；內容於此合併保存）

# Modern Agent

**Language:** [![中文](https://img.shields.io/badge/%E4%B8%AD%E6%96%87-%E4%B8%AD%E6%96%87%E7%89%88-blue?style=flat-square)](README.md) [![English](https://img.shields.io/badge/English-English-blue?style=flat-square)](README.en.md)

[![Python](https://img.shields.io/badge/Python-3.10-%233776AB?logo=python)]()
[![Status](https://img.shields.io/badge/Status-Planning-blue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

現代化智慧體（Agent）框架的實驗與規劃倉庫，探索工具使用、情境記憶管理與多模型整合的設計方法。

## 狀態

> **規劃中**：目前為架構探索與設計草稿階段，尚無完整可執行的實作。

## 研究方向

| 主題 | 說明 |
|------|------|
| 工具使用（Tool Use） | 如何讓智慧體安全且有效地呼叫外部工具 |
| 情境記憶管理 | 長期 / 短期記憶的儲存、檢索與更新策略 |
| 多模型整合 | 不同模型的任務分工與協調機制 |
| 任務規劃 | 複雜任務的分解、排序與執行追蹤 |

## 規劃架構

```
Modern_agent/
├── docs/           # 設計文件與研究筆記
├── experiments/    # 小型概念驗證
├── framework/      # 框架原型
└── README.md
```

## 相關專案

本倉庫屬於 Agent 研究系列，三者分工如下：

| 倉庫 | 定位 |
| --- | --- |
| [Modern_agent](https://github.com/TeWei02/Modern_agent) | 框架層設計：工具使用、情境記憶管理、多模型整合 |
| [UNIVERSAAL_AGENT](https://github.com/TeWei02/UNIVERSAAL_AGENT) | 通用型架構：跨領域任務規劃、工具整合與知識管理 |
| [agent_full](https://github.com/TeWei02/agent_full) | 落地實驗：macOS 本地模型與 RAG 的實作紀錄 |

## License

MIT © [Te-Wei Ko](https://github.com/TeWei02)
