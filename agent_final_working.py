import os
import asyncio
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

# 定義工具
pdf_tool = QueryEngineTool(
    query_engine=query_engine,
    metadata=ToolMetadata(name="search_pdf", description="搜尋PDF文件內容")
)

def calculate(expression: str) -> str:
    '''執行數學計算'''
    try:
        return f"計算: {expression} = {eval(expression)}"
    except Exception as e:
        return f"錯誤: {e}"

def get_time() -> str:
    '''獲取當前時間'''
    return datetime.datetime.now().strftime('當前時間: %Y年%m月%d日 %H:%M:%S')

def get_stats() -> str:
    '''獲取文件統計'''
    total_words = sum(len(d.text.split()) for d in documents)
    return f"文件統計 - 文件數: {len(documents)}, 總字數: {total_words:,}"

calculator_tool = FunctionTool.from_defaults(fn=calculate, name="calculator", description="數學計算")
time_tool = FunctionTool.from_defaults(fn=get_time, name="get_time", description="查詢時間")
stats_tool = FunctionTool.from_defaults(fn=get_stats, name="doc_stats", description="文件統計")

tools = [pdf_tool, calculator_tool, time_tool, stats_tool]

print("⚙️  建立 Agent...")
agent = ReActAgent(
    name="ModernReader_Agent",
    tools=tools,
    llm=llm,
    verbose=True
)
print("✅ Agent 已啟動\n")

# 測試函數
async def test_agent():
    print("="*60)
    print("🧪 自動測試")
    print("="*60 + "\n")
    
    tests = [
        "現在幾點？",
        "計算 10 + 20",
        "這個文件有多少字？",
        "PDF講什麼內容？"
    ]
    
    for i, test in enumerate(tests, 1):
        print(f"📝 測試 {i}: {test}")
        try:
            result = await agent.run(input=test)
            print(f"✅ 回答: {result}\n")
        except Exception as e:
            print(f"❌ 錯誤: {e}\n")

# 互動函數
async def interactive_mode():
    print("\n" + "="*60)
    print("💬 進入互動模式 (輸入 exit 退出)")
    print("="*60 + "\n")
    
    while True:
        try:
            user_input = input("你: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("\n👋 再見！")
                break
            
            print("\n🤖 Agent 思考中...\n")
            result = await agent.run(input=user_input)
            print(f"💬 回答: {result}\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 已中斷")
            break
        except Exception as e:
            print(f"\n❌ 錯誤: {e}\n")

# 主函數
async def main():
    await test_agent()
    await interactive_mode()

# 執行
if __name__ == "__main__":
    asyncio.run(main())
