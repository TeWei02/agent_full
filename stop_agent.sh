#!/bin/bash

if [ -f agent.pid ]; then
    PID=$(cat agent.pid)
    echo "🛑 停止 Agent (PID: $PID)"
    kill $PID 2>/dev/null
    rm agent.pid
    echo "✅ 已停止"
else
    echo "⚠️  找不到運行中的 Agent"
fi
