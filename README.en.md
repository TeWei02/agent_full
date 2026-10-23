**Language:** [![English](https://img.shields.io/badge/English-English-blue?style=flat-square)](README.en.md) [![中文](https://img.shields.io/badge/%E4%B8%AD%E6%96%87-%E4%B8%AD%E6%96%87%E7%89%88-blue?style=flat-square)](README.md)

# Agent Full

[![Python](https://img.shields.io/badge/Python-3.10--3.12-%233776AB?logo=python)](https://www.python.org/)
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-%232088FF?logo=githubactions)](https://github.com/features/actions)
[![Status](https://img.shields.io/badge/Status-Experimental-orange)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An experimentation and note-taking repository for local language model agents, recording the process of building a personal assistant system on macOS with open-source models and retrieval-augmented generation (RAG).

## Status

> **Experimental**: these are personal experiment notes recording environment setup, dependency choices, and architecture planning — not yet a complete deliverable application.

## Contents

| Item | Description |
|------|-------------|
| Experiment notes | `data/notes.txt` — environment setup and implementation records |
| Project planning | `data/project.txt` — goals and architecture ideas for a local retrieval Q&A system |
| Dependency list | `requirements.txt` — cloud APIs (Groq / OpenAI) and local models (Ollama / LlamaIndex) |
| Continuous integration | `.github/workflows/` — flake8 + pytest CI flow for Python 3.10–3.12 |
| Config template | `.env.example` — API-key environment variable template |

## Technical Directions

- LLM inference: Groq / OpenAI APIs, plus local models via Ollama
- Semantic retrieval & knowledge-base Q&A: LlamaIndex vector retrieval
- Environment management: python-dotenv, Conda / pip

## Project Structure

```
agent_full/
├── .env.example            # environment variable template
├── requirements.txt        # Python dependencies
├── data/
│   ├── notes.txt           # experiment notes
│   └── project.txt         # project planning
└── .github/workflows/      # CI config
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
