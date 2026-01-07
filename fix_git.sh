#!/bin/bash

echo "🔧 修復 Git 遠端設定"

# 移除舊遠端
git remote remove origin 2>/dev/null

# 詢問正確的用戶名
read -p "請輸入你的 GitHub 用戶名: " USERNAME

# 設定新遠端
git remote add origin https://github.com/$USERNAME/agent_full.git

echo ""
echo "✅ 遠端已設定為: https://github.com/$USERNAME/agent_full.git"
echo ""
echo "請確保:"
echo "1. 倉庫已在 GitHub 上創建"
echo "2. 你有推送權限"
echo ""
read -p "準備好推送了嗎？(y/n): " READY

if [ "$READY" = "y" ]; then
    git push -u origin main
fi
