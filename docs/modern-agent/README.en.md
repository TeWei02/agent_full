> **Source**: [TeWei02/Modern_agent](https://github.com/TeWei02/Modern_agent) (planning repository, archived; content preserved here)

**Language:** [![English](https://img.shields.io/badge/English-English-blue?style=flat-square)](README.en.md) [![中文](https://img.shields.io/badge/%E4%B8%AD%E6%96%87-%E4%B8%AD%E6%96%87%E7%89%88-blue?style=flat-square)](README.md)

# Modern Agent

[![Python](https://img.shields.io/badge/Python-3.10-%233776AB?logo=python)]()
[![Status](https://img.shields.io/badge/Status-Planning-blue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An experimentation and planning repository for a modern agent framework, exploring design approaches for tool use, context memory management, and multi-model integration.

## Status

> **Planning**: currently in the architecture-exploration and design-draft stage, with no complete runnable implementation yet.

## Research Directions

| Topic | Description |
|-------|-------------|
| Tool Use | How to let agents call external tools safely and effectively |
| Context Memory Management | Storage, retrieval, and update strategies for long-term / short-term memory |
| Multi-Model Integration | Task division and coordination mechanisms across different models |
| Task Planning | Decomposition, sequencing, and execution tracking of complex tasks |

## Planned Structure

```
Modern_agent/
├── docs/           # design documents and research notes
├── experiments/    # small proof-of-concepts
├── framework/      # framework prototype
└── README.md
```

## Related Projects

This repository belongs to the Agent research series; the division of labor among the three:

| Repository | Role |
| --- | --- |
| [Modern_agent](https://github.com/TeWei02/Modern_agent) | Framework-layer design: tool use, context memory management, multi-model integration |
| [UNIVERSAAL_AGENT](https://github.com/TeWei02/UNIVERSAAL_AGENT) | General-purpose architecture: cross-domain task planning, tool integration, knowledge management |
| [agent_full](https://github.com/TeWei02/agent_full) | Hands-on experiments: implementation records for macOS local models and RAG |

## License

MIT © [Te-Wei Ko](https://github.com/TeWei02)
