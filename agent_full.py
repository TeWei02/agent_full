import os
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI

# ============ 1. 設定 API Keys ============
os.environ["OPENAI_API_KEY"] = "你的_OPENAI_API_KEY"
os.environ["LLAMA_CLOUD_API_KEY"] = "你的_LLAMA_CLOUD_API_KEY"

# ============ 2. 初始化 LlamaParse 文件解析器 ============
print("📄 初始化文件解析器...")
parser = LlamaParse(
    result_type="markdown",
    verbose=True
)

# ============ 3. 加載和解析文件 ============
print("📂 加載文件...")
# 方式1: 直接用 LlamaParse 解析
documents = []
pdf_files = ["sample.pdf"]  # 把你的 PDF 放在這裡

for pdf_file in pdf_files:
    if os.path.exists(pdf_file):
        print(f"  解析 {pdf_file}...")
        docs = parser.load_data(pdf_file)
        documents.extend(docs)
        print(f"  ✓ 成功解析 {len(docs)} 個文件")

# ============ 4. 建立 RAG 索引 ============
print("🔍 建立向量索引...")
if documents:
    index = VectorStoreIndex.from_documents(documents)
    print("  ✓ 索引建立完成")
else:
    print("  ⚠️  沒有文件可索引")
    index = VectorStoreIndex([])

# ============ 5. 建立查詢引擎 ============
print("🔧 設置查詢引擎...")
query_engine = index.as_query_engine(similarity_top_k=3)

# ============ 6. 建立 Tool for Agent ============
tools = [
    QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name="pdf_rag_tool",
            description="查詢已上傳的 PDF 文件內容，用於回答文件相關問題",
        ),
    ),
]

# ============ 7. 初始化 LLM ============
print("🤖 初始化 OpenAI LLM...")
llm = OpenAI(model="gpt-4", temperature=0.7)

# ============ 8. 建立 ReAct Agent ============
print("⚙️  建立 AI Agent...")
agent = ReActAgent.from_tools(
    tools,
    llm=llm,
    verbose=True,
    max_iterations=5,
)

# ============ 9. 測試 Agent ============
print("\n" + "="*50)
print("🎯 AI Agent 已準備就緒！")
print("="*50 + "\n")

# 範例查詢
test_queries = [
    "PDF 裡面主要講什麼？",
    "有沒有提到關於技術的內容？",
    "總結一下重點",
]

for query in test_queries:
    print(f"👤 用戶: {query}")
    try:
        response = agent.chat(query)
        print(f"🤖 Agent: {response}\n")
    except Exception as e:
        print(f"❌ 錯誤: {e}\n")

# ============ 10. 互動模式 ============
print("\n💬 進入互動模式 (輸入 'exit' 退出):")
while True:
    user_input = input("\n你: ").strip()
    if user_input.lower() == "exit":
        print("👋 再見!")
        break
    if not user_input:
        continue
    
    try:
        response = agent.chat(user_input)
        print(f"🤖 Agent: {response}")
    except Exception as e:
        print(f"❌ 錯誤: {e}")

