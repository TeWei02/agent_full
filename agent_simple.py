import os
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI

print("🚀 ModernReader AI Agent 啟動中...\n")

# ============ Step 1: 解析 PDF ============
print("📄 Step 1: 解析 PDF 文件...")
try:
    parser = LlamaParse(result_type="markdown", verbose=False)
    documents = parser.load_data("sample.pdf")
    print(f"✅ 成功解析 {len(documents)} 個文件\n")
except Exception as e:
    print(f"❌ 解析失敗: {e}")
    print("請確保 LLAMA_CLOUD_API_KEY 正確設定\n")
    exit(1)

# ============ Step 2: 建立索引 ============
print("🔍 Step 2: 建立向量索引...")
try:
    index = VectorStoreIndex.from_documents(documents)
    print("✅ 索引建立完成\n")
except Exception as e:
    print(f"❌ 索引建立失敗: {e}\n")
    exit(1)

# ============ Step 3: 建立查詢引擎 ============
print("🔧 Step 3: 設置查詢引擎...")
query_engine = index.as_query_engine(similarity_top_k=3)

# ============ Step 4: 建立 Agent Tool ============
tools = [
    QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name="pdf_search",
            description="搜尋 PDF 文件內容並回答相關問題",
        ),
    ),
]

# ============ Step 5: 初始化 LLM ============
print("🤖 Step 5: 初始化 OpenAI GPT-4...")
try:
    llm = OpenAI(model="gpt-4", temperature=0.7)
    print("✅ LLM 已連接\n")
except Exception as e:
    print(f"❌ OpenAI 連接失敗: {e}")
    exit(1)

# ============ Step 6: 建立 ReAct Agent ============
print("⚙️  Step 6: 建立 ReAct Agent...")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, max_iterations=5)
print("✅ Agent 已啟動\n")

# ============ Step 7: 自動測試 ============
print("="*60)
print("🎯 AI Agent 已準備好！開始提問吧")
print("="*60 + "\n")

queries = ["這個文件主要講什麼？", "有提到哪些技術？"]
for q in queries:
    print(f"👤 Q: {q}")
    print(f"🤖 A: {agent.chat(q)}\n")

# ============ Step 8: 互動模式 ============
while True:
    user_input = input("\n你 (輸入 exit 退出): ").strip()
    if user_input.lower() in ["exit", "quit"]: break
    if user_input: print(f"Agent: {agent.chat(user_input)}")
