import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.tools import QueryEngineTool, ToolMetadata, FunctionTool
from llama_index.core.agent import ReActAgent
from llama_index.llms.ollama import Ollama
from llama_index.llms.groq import Groq
from llama_index.embeddings.ollama import OllamaEmbedding
import datetime

print("🤖 ModernReader AI Agent 啟動中...\n")

# ============ 配置 ============
USE_GROQ = False
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
CURRENT_MODEL = "llama3:latest"

# ============ 設定 LLM ============
if USE_GROQ:
    print("🌐 使用 Groq...")
    os.environ["GROQ_API_KEY"] = GROQ_API_KEY
    llm = Groq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)
else:
    print(f"🖥️  使用 Ollama ({CURRENT_MODEL})...")
    llm = Ollama(model=CURRENT_MODEL, request_timeout=300.0)

Settings.llm = llm
Settings.embed_model = OllamaEmbedding(model_name=CURRENT_MODEL)
print("✅ LLM 已連接\n")

# ============ 載入文件 ============
print("📄 載入文件...")
documents = SimpleDirectoryReader(input_files=["sample.pdf"]).load_data()
index = VectorStoreIndex.from_documents(documents, show_progress=True)
query_engine = index.as_query_engine(similarity_top_k=3)
print("✅ 索引完成\n")

# ============ 定義工具 ============
pdf_tool = QueryEngineTool(
    query_engine=query_engine,
    metadata=ToolMetadata(
        name="search_pdf",
        description="搜尋 PDF 文件內容，回答關於文件的問題"
    ),
)

def calculate(expression: str) -> str:
    """執行數學計算
    
    Args:
        expression: 數學表達式，例如 "2+3*4"
    
    Returns:
        計算結果
    """
    try:
        result = eval(expression)
        return f"計算結果: {expression} = {result}"
    except Exception as e:
        return f"計算錯誤: {str(e)}"

calculator_tool = FunctionTool.from_defaults(
    fn=calculate,
    name="calculator",
    description="執行數學計算，輸入數學表達式"
)

def get_time() -> str:
    """獲取當前時間和日期
    
    Returns:
        當前的日期和時間
    """
    now = datetime.datetime.now()
    weekdays = ['週一', '週二', '週三', '週四', '週五', '週六', '週日']
    weekday = weekdays[now.weekday()]
    return f"當前時間: {now.strftime('%Y年%m月%d日')} {weekday} {now.strftime('%H:%M:%S')}"

time_tool = FunctionTool.from_defaults(
    fn=get_time,
    name="get_time",
    description="獲取當前的日期、時間和星期"
)

def get_stats() -> str:
    """獲取文件統計資訊
    
    Returns:
        文件的統計數據
    """
    total_chars = sum(len(doc.text) for doc in documents)
    total_words = sum(len(doc.text.split()) for doc in documents)
    return f"""文件統計:
- 文件數量: {len(documents)} 個
- 總字元數: {total_chars:,}
- 總單字數: {total_words:,}"""

stats_tool = FunctionTool.from_defaults(
    fn=get_stats,
    name="doc_stats",
    description="獲取載入文件的統計資訊"
)

def modernreader_info() -> str:
    """說明 ModernReader 系統的功能
    
    Returns:
        ModernReader 的功能介紹
    """
    return """ModernReader 核心功能:

1. 多感官閱讀體驗
   - 視覺: 可調整字體、顏色
   - 聽覺: AI 語音朗讀
   - 觸覺: 觸覺反饋輔助

2. AI 智能輔助
   - 內容摘要與重點提取
   - 智能問答系統
   - 個性化推薦

3. 無障礙設計
   - 支援視覺障礙者
   - 閱讀困難者輔助
   - 多語言支援

4. 技術架構
   - LlamaIndex RAG 系統
   - LlamaParse 文件解析
   - Ollama/Groq LLM 支援"""

features_tool = FunctionTool.from_defaults(
    fn=modernreader_info,
    name="modernreader_info",
    description="說明 ModernReader 系統的完整功能"
)

tools = [pdf_tool, calculator_tool, time_tool, stats_tool, features_tool]

# ============ 建立 ReAct Agent（正確方式）============
print("⚙️  建立 ReAct Agent...")

agent = ReActAgent(
    name="ModernReader Agent",
    description="ModernReader 的 AI 助手，可以搜尋文件、執行計算、查詢時間等",
    tools=tools,
    llm=llm,
    verbose=True,
)

print("✅ Agent 已啟動\n")

# ============ 自動測試 ============
print("="*60)
print("🧪 測試 Agent 推理能力")
print("="*60 + "\n")

tests = [
    "現在幾點？",
    "計算 (15 + 25) * 3",
    "這個文件有多少字？",
    "ModernReader 有哪些核心功能？",
    "這個 PDF 主要講什麼內容？"
]

for i, test in enumerate(tests, 1):
    print(f"\n{'='*60}")
    print(f"📝 任務 {i}/{len(tests)}: {test}")
    print('='*60)
    try:
        response = agent.chat(test)
        print(f"\n✅ Agent 回答:\n{response.response}\n")
    except Exception as e:
        print(f"❌ 錯誤: {e}\n")

# ============ 互動模式 ============
print("\n" + "="*60)
print("💬 Agent 互動模式")
print("="*60)
print("\n🔧 Agent 能力:")
print("  📄 search_pdf      - 搜尋 PDF 內容")
print("  🧮 calculator      - 數學計算")
print("  ⏰ get_time        - 查詢時間")
print("  📊 doc_stats       - 文件統計")
print("  💡 modernreader    - 功能說明")
print("\n📋 指令:")
print("  'tools'   - 查看所有工具")
print("  'switch'  - 切換 LLM")
print("  'exit'    - 退出\n")

while True:
    try:
        user_input = input("你: ").strip()
        
        if not user_input:
            continue
            
        if user_input.lower() in ['exit', 'quit', 'q']:
            print("\n👋 感謝使用 ModernReader AI Agent！再見~")
            break
        
        if user_input.lower() == 'tools':
            print("\n🔧 可用工具清單:\n")
            for i, tool in enumerate(tools, 1):
                print(f"{i}. {tool.metadata.name}")
                print(f"   📝 {tool.metadata.description}\n")
            continue
        
        if user_input.lower() == 'switch':
            USE_GROQ = not USE_GROQ
            if USE_GROQ:
                llm = Groq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)
                print("✅ 已切換到 Groq 雲端 API\n")
            else:
                llm = Ollama(model=CURRENT_MODEL, request_timeout=300.0)
                print(f"✅ 已切換到 Ollama 本地模型 ({CURRENT_MODEL})\n")
            Settings.llm = llm
            agent = ReActAgent(
                name="ModernReader Agent",
                tools=tools,
                llm=llm,
                verbose=True
            )
            continue
        
        # Agent 執行任務
        print("\n🤖 Agent 思考中...\n")
        response = agent.chat(user_input)
        print(f"\n💬 Agent: {response.response}\n")
        
    except KeyboardInterrupt:
        print("\n\n👋 程式已中斷，再見！")
        break
    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}\n")

