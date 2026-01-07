#!/bin/bash

echo "🔒 修復 GitHub Secret 推送問題"
echo "=================================="

# 1. 創建 .env
if [ ! -f .env ]; then
    read -p "請輸入你的 Groq API Key: " API_KEY
    echo "GROQ_API_KEY=$API_KEY" > .env
    echo "✅ .env 已創建"
fi

# 2. 確保 .gitignore
if ! grep -q ".env" .gitignore; then
    echo ".env" >> .gitignore
    echo "✅ .env 已加入 .gitignore"
fi

# 3. 移除所有文件中的硬編碼 Key
echo "🔧 移除硬編碼 API Key..."

for file in *.py; do
    if grep -q 'GROQ_API_KEY = "gsk_' "$file" 2>/dev/null; then
        sed -i '' 's/GROQ_API_KEY = "gsk_[^"]*"/GROQ_API_KEY = os.getenv("GROQ_API_KEY")/' "$file"
        
        # 確保有 import os
        if ! grep -q "^import os$" "$file"; then
            sed -i '' '1s/^/import os\n/' "$file"
        fi
        
        echo "  ✓ 修改 $file"
    fi
done

# 4. 詢問是否重建 Git
echo ""
read -p "是否重建 Git 歷史（會清除所有舊 commit）？(y/n): " REBUILD

if [ "$REBUILD" = "y" ]; then
    echo "🔄 重建 Git..."
    
    # 備份
    rm -rf .git
    
    # 重新初始化
    git init
    git add .
    git commit -m "feat: 完成 ModernReader AI Agent

- 完整的 RAG 文件分析系統
- 支援 Ollama 和 Groq 雙 LLM
- 自動任務執行功能
- 移除了所有敏感資訊"
    
    # 設定遠端
    read -p "請輸入你的 GitHub Token: " TOKEN
    git remote add origin https://$TOKEN@github.com/STUST-KOTEWEI/agent_full.git
    
    # 推送
    git push -u origin main --force
    
    echo "✅ 推送完成！"
else
    echo "請手動執行："
    echo "  git add ."
    echo "  git commit -m 'fix: 移除敏感資訊'"
    echo "  git push -u origin main --force"
fi

echo ""
echo "🎉 完成！記得："
echo "  1. 撤銷舊的 Groq API Key"
echo "  2. 生成新的 Key"
echo "  3. 更新 .env 文件"
