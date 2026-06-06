<!-- omit in toc -->
# agent_full — Autonomous AI Agent Framework

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/LLM-Groq-F56945?logo=groq)](https://groq.com/)
[![Ollama](https://img.shields.io/badge/Local-Ollama-000000?logo=ollama)](https://ollama.com/)
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions)](https://github.com/TeWei02/agent_full/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight autonomous AI agent framework that combines cloud LLM (Groq) speed with local RAG capabilities via Ollama + LlamaIndex. Designed for rapid prototyping on macOS, with full GitHub integration.

> **Note:** This repository consolidates the previous `Modern_agent` and `UNIVERSAAL_AGENT` projects, which have been archived as historical references.

## Table of Contents

- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Tech Stack](#tech-stack)
- [CI/CD](#cicd)
- [License](#license)

## Architecture

```
┌──────────────────────────────────────────────┐
│                  agent_full                   │
├──────────┬──────────────────┬────────────────┤
│ Agent    │ LLM Backend      │ Tool Layer     │
│ Core     │ Groq API         │ GitHub API     │
│          │ Ollama (local)   │ File System    │
│          │ LlamaIndex (RAG) │ Web Search     │
├──────────┴──────────────────┴────────────────┤
│              Memory & Context                  │
│         File-based persistence layer           │
└──────────────────────────────────────────────┘
```

| Component | Responsibility | Technology |
|-----------|---------------|------------|
| Agent Core | Prompt-based autonomous task execution | Python |
| Cloud LLM | High-speed inference via Groq API | Groq (Mixtral / Llama) |
| Local LLM | Private on-device inference | Ollama |
| RAG Engine | Vector-based document retrieval | LlamaIndex |
| Tool Integration | External API & filesystem interactions | GitHub API, REST |
| Memory | Session & task context persistence | File-based JSON |

## Quick Start

```bash
# Clone
git clone https://github.com/TeWei02/agent_full
cd agent_full

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Configure
cp .env.example .env
# Edit .env — add your Groq API key and GitHub token

# Run (module entry point)
python -m agent_full
```

## Project Structure

```
agent_full/
├── agent_full/              # Agent core package
│   ├── __init__.py
│   ├── agent.py             # Autonomous agent loop
│   ├── llm.py               # LLM backend abstraction
│   ├── tools.py             # Tool integrations (GitHub, FS)
│   └── memory.py            # Context persistence
├── data/                    # Memory & context files
├── .github/workflows/       # CI pipeline
├── .env.example             # API key template
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
```

## Configuration

Copy the environment template and fill in your credentials:

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Groq API key for cloud LLM | Yes |
| `GITHUB_TOKEN` | GitHub personal access token | Yes |

```bash
cp .env.example .env
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Language** | Python 3.10+ |
| **Cloud LLM** | Groq (Mixtral, Llama series) |
| **Local LLM** | Ollama |
| **RAG** | LlamaIndex |
| **CI/CD** | GitHub Actions (pytest + flake8) |
| **Platform** | macOS (primary), cross-platform |

## CI/CD

GitHub Actions pipeline runs on every push and PR:

- **Python versions:** 3.10, 3.11, 3.12
- **Linting:** flake8 (syntax errors + complexity check)
- **Testing:** pytest

See [.github/workflows/python-package-conda.yml](.github/workflows/python-package-conda.yml) for details.

## License

MIT © [TeWei02](https://github.com/TeWei02)
