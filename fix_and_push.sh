#!/bin/bash

echo "🔧 修復並推送到正確的倉庫"
echo "=================================="

# 1. 移除舊遠端
git remote remove origin 2>/dev/null

# 2. 讀取 Token
read -p "請輸入你的 GitHub Token: " TOKEN

# 3. 添加正確的遠端（TeWei02）
git remote add origin https://$TOKEN@github.com/TeWei02/agent_full.git

echo "✅ 遠端已設定為: https://github.com/TeWei02/agent_full.git"

# 4. 確保有 commit
if ! git log &>/dev/null; then
    echo "📝 創建初始提交..."
    git add .
    git commit -m "feat: 完成 ModernReader AI Agent

- LlamaIndex RAG 文件分析系統  
- 支援 Ollama 和 Groq 雙 LLM
- 自動任務執行功能
- Web UI 介面
- 完整的工具系統（PDF搜尋、計算、時間等）"
fi

# 5. 確保在 main 分支
git branch -M main

# 6. 推送
echo "🚀 開始推送..."
git push -u origin main --force

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 成功推送到 https://github.com/TeWei02/agent_full"
    echo ""
    echo "⚠️  記得："
    echo "  1. 撤銷舊的 Groq API Key"  
    echo "  2. 前往 https://console.groq.com/keys"
    echo "  3. 刪除洩露的 Key，生成新的"
    echo "  4. 更新 .env 文件"
else
    echo ""
    echo "❌ 推送失敗，請檢查錯誤訊息"
fi
