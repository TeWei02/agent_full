#!/bin/bash

echo "🚀 啟動 ModernReader AI Agent"

# 啟動虛擬環境
source agent-env/bin/activate

# 啟動 Ollama（如果需要）
if ! pgrep -x "ollama" > /dev/null; then
    echo "🔧 啟動 Ollama..."
    ollama serve &
    sleep 3
fi

# 選擇模式
echo ""
echo "選擇啟動模式:"
echo "1. 完整版 (agent_complete.py)"
echo "2. 自動版 (agent_auto.py)"
echo ""

read -p "請選擇 (1/2): " choice

if [ "$choice" = "1" ]; then
    python agent_complete.py
else
    python agent_auto.py
fi
