from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.ollama import Ollama
from llama_index.core.embeddings import resolve_embed_model
from llama_index.core import Settings

print("🚀 免費 AI Agent 啟動中...\n")

# ============ 設定免費 LLM ============
print("🤖 連接本地 Ollama...")
Settings.llm = Ollama(model="llama3.2:3b", request_timeout=120.0)
Settings.embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")
print("✅ 本地模型已載入\n")

# ============ 載入 PDF ============
print("📄 載入 PDF...")
documents = SimpleDirectoryReader(
    input_files=["sample.pdf"]
).load_data()
print(f"✅ 已載入 {len(documents)} 個文件\n")

# ============ 建立索引 ============
print("🔍 建立向量索引...")
index = VectorStoreIndex.from_documents(documents)
print("✅ 索引建立完成\n")

# ============ 查詢引擎 ============
query_engine = index.as_query_engine()

# ============ 測試 ============
print("="*60)
print("🎯 免費 AI Agent 已準備好！")
print("="*60 + "\n")

test_queries = [
    "這個文件主要講什麼？",
    "有提到哪些技術？"
]

for q in test_queries:
    print(f"👤 Q: {q}")
    response = query_engine.query(q)
    print(f"🤖 A: {response}\n")

# ============ 互動模式 ============
print("💬 進入互動模式 (輸入 exit 退出)\n")
while True:
    user_input = input("你: ").strip()
    if user_input.lower() in ['exit', 'quit']: break
    if user_input:
        response = query_engine.query(user_input)
        print(f"🤖 {response}\n")

