#!/bin/bash

echo "🔄 完全重置 Git 歷史"
echo "====================="

# 1. 備份
echo "📦 備份代碼..."
mkdir -p ../agent_backup
cp -r * ../agent_backup/ 2>/dev/null

# 2. 刪除 Git 歷史
echo "🗑️  刪除舊的 Git 歷史..."
rm -rf .git

# 3. 重新初始化
echo "🆕 重新初始化..."
git init
git add .
git commit -m "feat: ModernReader AI Agent 初始版本

功能：
- LlamaIndex RAG 文件分析
- Ollama/Groq 雙 LLM 支援  
- 自動任務執行系統
- Web UI 介面

注意：所有敏感資訊已移除，請配置 .env 文件"

# 4. 設定遠端（用新的 Token）
echo ""
read -p "請輸入【新的】GitHub Token: " NEW_TOKEN

git remote add origin https://$NEW_TOKEN@github.com/TeWei02/agent_full.git

# 5. 強制推送
echo "🚀 推送..."
git push -u origin main --force

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 成功！"
    echo ""
    echo "✅ 下一步："
    echo "  1. 生成新的 Groq API Key"
    echo "  2. 創建 .env 文件（參考 .env.example）"
    echo "  3. 填入新的 API Key"
else
    echo ""
    echo "❌ 失敗，請手動檢查"
fi
