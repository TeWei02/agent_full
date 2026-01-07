#!/bin/bash

echo "🚀 ModernReader AI Agent - 一鍵安裝"
echo "======================================"

# 檢查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 未安裝 Python 3"
    exit 1
fi

echo "✅ Python 已安裝"

# 創建虛擬環境
echo "📦 創建虛擬環境..."
python3 -m venv agent-env
source agent-env/bin/activate

# 安裝套件
echo "📥 安裝依賴套件..."
pip install --upgrade pip
pip install llama-index-core llama-index-llms-ollama llama-index-llms-groq \
    llama-index-embeddings-ollama chromadb gradio

# 檢查 Ollama
if ! command -v ollama &> /dev/null; then
    echo "⚠️  Ollama 未安裝，正在安裝..."
    brew install ollama
fi

echo "✅ 安裝完成！"
echo ""
echo "使用方法："
echo "  source agent-env/bin/activate"
echo "  python agent_complete.py"
