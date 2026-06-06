# agent_full — Autonomous AI Agent Framework

[![Python](https://img.shields.io/badge/Python-3-%233776AB?logo=python)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/LLM-Groq-%23F56945)](https://groq.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight autonomous AI agent framework powered by Groq's high-speed inference API. Designed for local Mac development with GitHub integration.

## Architecture

| Component | Responsibility |
|-----------|---------------|
| Agent Core | Prompt-based autonomous task execution |
| LLM Backend | Groq API (Mixtral / Llama models) |
| Tool Integration | GitHub API via token-based auth |
| Memory | File-based context persistence |

## Quick Start

```bash
# Clone and set up
git clone https://github.com/TeWei02/agent_full
cd agent_full

# Configure
cp .env.example .env
# Edit .env with your Groq API key and GitHub token

# Install
pip install -r requirements.txt

# Run
python -m agent_full
```

## Project Structure

```
agent_full/
├── agent_full/        # Agent core module
├── data/              # Memory & context files
├── .env.example       # API key template
└── README.md
```

## License

MIT
