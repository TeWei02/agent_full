#!/bin/bash

echo "🔒 清理所有敏感資訊..."

# 刪除包含 API Key 的文件
rm -f agent_groq.py

# 檢查所有 Python 文件中的 Key
echo "檢查所有 .py 文件..."
grep -r "gsk_" *.py 2>/dev/null && echo "⚠️ 發現 Groq Key!" || echo "✅ 沒有 Groq Key"
grep -r "ghp_" *.py 2>/dev/null && echo "⚠️ 發現 GitHub Token!" || echo "✅ 沒有 GitHub Token"

# 創建 .env 模板
cat > .env.example << 'ENVEOF'
# 複製這個文件為 .env 並填入你的密鑰
GROQ_API_KEY=你的_Groq_API_Key
GITHUB_TOKEN=你的_GitHub_Token
ENVEOF

# 確保 .gitignore 正確
cat > .gitignore << 'GITEOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
llm-env/
agent-env/
*.egg-info/
dist/
build/

# 敏感資訊
.env
*.key
*_KEY*
*.token

# 資料
*.pdf
*.log
task_report.md
chroma_data/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# macOS
.DS_Store

# Backup
*_backup/
GITEOF

echo "✅ 清理完成！"
