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
| Planning docs | `docs/` — merged content of archived planning repositories (framework design / general architecture) |
| Experiments | `experiments/` — reserved for future proof-of-concepts and experiment scripts |
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
├── docs/
│   ├── modern-agent/       # framework-layer design (formerly Modern_agent, archived)
│   └── universaal-agent/   # general-purpose architecture (formerly UNIVERSAAL_AGENT, archived)
├── experiments/            # proof-of-concepts and experiments (reserved)
└── .github/workflows/      # CI config
```

## Archived Planning Repositories, Content Merged Here

The planning repositories of the Agent research series — **Modern_agent** (framework-layer design: tool use, context memory management, multi-model integration) and **UNIVERSAAL_AGENT** (general-purpose architecture: cross-domain task planning, tool integration, knowledge management) — were archived on 2026-10-24, and their planning documents have been merged into the `docs/` directory of this repository with source attribution preserved.

| Original repository | Role | Merge location |
| --- | --- | --- |
| Modern_agent (archived) | Framework-layer design: tool use, context memory management, multi-model integration | [docs/modern-agent/](docs/modern-agent/) |
| UNIVERSAAL_AGENT (archived) | General-purpose architecture: cross-domain task planning, tool integration, knowledge management | [docs/universaal-agent/](docs/universaal-agent/) |
| agent_full (this repo) | Hands-on experiments: implementation records for macOS local models and RAG | — |

This repository is now the single main repository of the Agent research series, covering hands-on experiments, architecture planning, and framework design.

## License

MIT © [Te-Wei Ko](https://github.com/TeWei02)
