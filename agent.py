import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.tools import QueryEngineTool, ToolMetadata, FunctionTool
from llama_index.core.agent import ReActAgent
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
import datetime

print("🤖 ModernReader AI Agent 啟動中...\n")

CURRENT_MODEL = "llama3:latest"
llm = Ollama(model=CURRENT_MODEL, request_timeout=300.0)
Settings.llm = llm
Settings.embed_model = OllamaEmbedding(model_name=CURRENT_MODEL)
print("✅ LLM 已連接\n")

print("📄 載入文件...")
documents = SimpleDirectoryReader(input_files=["sample.pdf"]).load_data()
index = VectorStoreIndex.from_documents(documents, show_progress=True)
query_engine = index.as_query_engine(similarity_top_k=3)
print("✅ 索引完成\n")

pdf_tool = QueryEngineTool(
    query_engine=query_engine,
    metadata=ToolMetadata(name="search_pdf", description="搜尋PDF內容")
)

def calculate(expression: str) -> str:
    try:
        return f"計算結果: {expression} = {eval(expression)}"
    except Exception as e:
        return f"錯誤: {e}"

def get_time() -> str:
    now = datetime.datetime.now()
    return f"當前時間: {now.strftime('%Y年%m月%d日 %H:%M:%S')}"

def get_stats() -> str:
    total_words = sum(len(d.text.split()) for d in documents)
    return f"文件數: {len(documents)}, 總字數: {total_words:,}"

calculator_tool = FunctionTool.from_defaults(fn=calculate, name="calculator", description="數學計算")
time_tool = FunctionTool.from_defaults(fn=get_time, name="get_time", description="查詢時間")
stats_tool = FunctionTool.from_defaults(fn=get_stats, name="doc_stats", description="文件統計")

tools = [pdf_tool, calculator_tool, time_tool, stats_tool]

print("⚙️  建立 Agent...")
agent = ReActAgent(
    name="ModernReader Agent",
    tools=tools,
    llm=llm,
    verbose=True
)
print("✅ Agent 已啟動\n")

print("="*60)
print("🧪 自動測試")
print("="*60 + "\n")

tests = ["現在幾點？", "計算 10+20", "文件有多少字？", "這個PDF講什麼？"]
for i, test in enumerate(tests, 1):
    print(f"\n📝 測試 {i}: {test}")
    try:
        response = agent.chat(test)
        print(f"✅ {response.response}\n")
    except Exception as e:
        print(f"❌ {e}\n")

print("\n💬 互動模式 (輸入 exit 退出)\n")
while True:
    try:
        q = input("你: ").strip()
        if not q:
            continue
        if q.lower() in ['exit', 'quit']:
            print("\n👋 再見！")
            break
        response = agent.chat(q)
        print(f"\n🤖 {response.response}\n")
    except KeyboardInterrupt:
        print("\n\n👋 已中斷")
        break
    except Exception as e:
        print(f"\n❌ 錯誤: {e}\n")
