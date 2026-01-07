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

documents = SimpleDirectoryReader(input_files=["sample.pdf"]).load_data()
index = VectorStoreIndex.from_documents(documents, show_progress=True)
query_engine = index.as_query_engine(similarity_top_k=3)

pdf_tool = QueryEngineTool(query_engine=query_engine, metadata=ToolMetadata(name="search_pdf", description="搜尋PDF"))

def calculate(expression: str) -> str:
    try: return f"{expression} = {eval(expression)}"
    except Exception as e: return f"錯誤: {e}"

def get_time() -> str:
    return datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')

def get_stats() -> str:
    return f"文件數: {len(documents)}, 字數: {sum(len(d.text.split()) for d in documents):,}"

calculator_tool = FunctionTool.from_defaults(fn=calculate, name="calc", description="計算")
time_tool = FunctionTool.from_defaults(fn=get_time, name="time", description="時間")
stats_tool = FunctionTool.from_defaults(fn=get_stats, name="stats", description="統計")

tools = [pdf_tool, calculator_tool, time_tool, stats_tool]
agent = ReActAgent(name="Agent", tools=tools, llm=llm, verbose=True)

print("✅ Agent 已啟動\n")

tests = ["現在幾點？", "計算 10+20", "文件統計", "PDF講什麼？"]
for test in tests:
    print(f"\nQ: {test}")
    print(f"A: {agent.chat(test).response}\n")

print("\n💬 互動模式 (exit退出)\n")
while True:
    q = input("你: ").strip()
    if q.lower() in ['exit', 'quit']: break
    if q: print(f"\n🤖 {agent.chat(q).response}\n")
