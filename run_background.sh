#!/bin/bash

# 後台運行 Agent

echo "🚀 啟動 AI Agent（後台模式）"

# 啟動虛擬環境
source llm-env/bin/activate

# 確保 Ollama 運行
if ! pgrep -x "ollama" > /dev/null; then
    echo "🔧 啟動 Ollama..."
    ollama serve > /dev/null 2>&1 &
    sleep 3
fi

# 後台運行 Agent
nohup python agent_auto.py > agent.log 2>&1 &
AGENT_PID=$!

echo "✅ Agent 已啟動（PID: $AGENT_PID）"
echo "📝 日誌文件: agent.log"
echo ""
echo "管理指令:"
echo "  查看日誌: tail -f agent.log"
echo "  停止服務: kill $AGENT_PID"

# 保存 PID
echo $AGENT_PID > agent.pid
