import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.tools import QueryEngineTool, ToolMetadata, FunctionTool
from llama_index.core.agent import FunctionCallingAgentWorker, AgentRunner
from llama_index.llms.ollama import Ollama
from llama_index.llms.groq import Groq
from llama_index.embeddings.ollama import OllamaEmbedding
import datetime

print("🤖 ModernReader 真正的 AI Agent 啟動中...\n")

# ============ 配置 ============
USE_GROQ = False
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
CURRENT_MODEL = "llama3:latest"

# ============ 設定 LLM ============
if USE_GROQ:
    print("🌐 使用 Groq 雲端 API...")
    os.environ["GROQ_API_KEY"] = GROQ_API_KEY
    llm = Groq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)
else:
    print(f"🖥️  使用本地 Ollama ({CURRENT_MODEL})...")
    llm = Ollama(model=CURRENT_MODEL, request_timeout=300.0)

Settings.llm = llm
Settings.embed_model = OllamaEmbedding(model_name=CURRENT_MODEL)
print("✅ LLM 已連接\n")

# ============ 載入 PDF 並建立索引 ============
print("📄 載入文件並建立索引...")
documents = SimpleDirectoryReader(input_files=["sample.pdf"]).load_data()
index = VectorStoreIndex.from_documents(documents, show_progress=True)
query_engine = index.as_query_engine(similarity_top_k=3)
print("✅ 索引完成\n")

# ============ 定義工具 ============
# 工具 1: PDF 查詢
pdf_tool = QueryEngineTool(
    query_engine=query_engine,
    metadata=ToolMetadata(
        name="search_pdf",
        description="搜尋 PDF 文件內容，回答關於文件的問題。適用於查找文件資訊、理解內容、摘要重點。"
    ),
)

# 工具 2: 計算器
def calculate(expression: str) -> str:
    """
    執行數學計算
    Args:
        expression: 數學表達式，例如 "2+3*4"
    """
    try:
        result = eval(expression)
        return f"計算結果: {expression} = {result}"
    except Exception as e:
        return f"計算錯誤: {str(e)}"

calculator_tool = FunctionTool.from_defaults(
    fn=calculate,
    name="calculator",
    description="執行數學計算，輸入數學表達式例如: 2+3*4 或 (10-5)/2"
)

# 工具 3: 時間查詢
def get_current_time() -> str:
    """獲取當前時間和日期"""
    now = datetime.datetime.now()
    weekdays = ['週一', '週二', '週三', '週四', '週五', '週六', '週日']
    weekday = weekdays[now.weekday()]
    return f"當前時間: {now.strftime('%Y年%m月%d日')} {weekday} {now.strftime('%H:%M:%S')}"

time_tool = FunctionTool.from_defaults(
    fn=get_current_time,
    name="get_time",
    description="獲取當前的日期、時間和星期幾"
)

# 工具 4: 文件統計
def document_stats() -> str:
    """獲取載入文件的詳細統計資訊"""
    total_chars = sum(len(doc.text) for doc in documents)
    total_words = sum(len(doc.text.split()) for doc in documents)
    avg_words = total_words // len(documents) if documents else 0
    
    return f"""📊 文件統計資訊:
━━━━━━━━━━━━━━━━━━━━
📄 文件數量: {len(documents)} 個
📝 總字元數: {total_chars:,} 字元
🔤 總單字數: {total_words:,} 個
📈 平均字數: {avg_words:,} 字/文件
━━━━━━━━━━━━━━━━━━━━"""

stats_tool = FunctionTool.from_defaults(
    fn=document_stats,
    name="doc_stats",
    description="獲取載入文件的統計資訊，包括數量、字數等"
)

# 工具 5: ModernReader 功能
def modernreader_features() -> str:
    """說明 ModernReader 系統的核心功能和架構"""
    return """🚀 ModernReader 系統功能介紹

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 核心功能
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. 多感官閱讀體驗 👁️👂✋
   • 視覺: 可調整字體、大小、間距、顏色
   • 聽覺: AI 語音朗讀，自然發音
   • 觸覺: 觸覺反饋輔助理解

2. AI 智能輔助 🤖
   • 自動內容摘要與重點提取
   • 智能問答系統
   • 個性化內容推薦
   • 閱讀理解輔助

3. 無障礙設計 ♿
   • 視覺障礙者支援
   • 閱讀困難者輔助
   • 學習障礙友善
   • 多語言支援

4. 技術架構 ⚙️
   • LlamaIndex RAG 系統
   • LlamaParse 高精度文件解析
   • Ollama/Groq 本地/雲端 LLM
   • 向量資料庫高效檢索
   • Chroma 持久化存儲

━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

features_tool = FunctionTool.from_defaults(
    fn=modernreader_features,
    name="modernreader_info",
    description="提供 ModernReader 系統的完整功能介紹和技術架構說明"
)

# ============ 建立 Function Calling Agent ============
print("⚙️  建立 Function Calling Agent...")
tools = [pdf_tool, calculator_tool, time_tool, stats_tool, features_tool]

agent_worker = FunctionCallingAgentWorker.from_tools(
    tools,
    llm=llm,
    verbose=True,
    allow_parallel_tool_calls=False,
)

agent = AgentRunner(agent_worker)
print("✅ Agent 已啟動\n")

# ============ 自動測試 Agent 能力 ============
print("="*60)
print("🧪 測試 Agent 的推理和工具使用能力")
print("="*60 + "\n")

test_tasks = [
    "現在幾點？今天星期幾？",
    "計算 (15 + 25) * 3 - 10",
    "這個文件有多少字？給我詳細統計",
    "ModernReader 有哪些核心功能？",
    "這個 PDF 主要講什麼內容？請簡單總結"
]

for i, task in enumerate(test_tasks, 1):
    print(f"\n{'='*60}")
    print(f"📝 任務 {i}/{len(test_tasks)}: {task}")
    print('='*60)
    try:
        response = agent.chat(task)
        print(f"\n✅ Agent 回答:\n{response}\n")
    except Exception as e:
        print(f"❌ 錯誤: {e}\n")

# ============ 互動模式 ============
print("\n" + "="*60)
print("💬 進入 Agent 互動模式")
print("="*60)
print("\n🔧 Agent 擁有以下能力:")
print("  📄 search_pdf     - 搜尋 PDF 內容")
print("  🧮 calculator     - 數學計算")
print("  ⏰ get_time       - 查詢時間")
print("  📊 doc_stats      - 文件統計")
print("  💡 modernreader   - 功能說明")
print("\n📋 可用指令:")
print("  'tools'   - 查看所有工具詳情")
print("  'switch'  - 切換 LLM (Groq ↔ Ollama)")
print("  'model'   - 查看當前模型")
print("  'exit'    - 退出程式")
print("\n💡 提示: Agent 會自動選擇合適的工具來回答你的問題\n")

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
        
        if user_input.lower() == 'model':
            model_type = "Groq (雲端)" if USE_GROQ else f"Ollama (本地)"
            model_name = "llama-3.3-70b-versatile" if USE_GROQ else CURRENT_MODEL
            print(f"\n📊 當前配置:")
            print(f"  LLM 類型: {model_type}")
            print(f"  模型名稱: {model_name}")
            print(f"  工具數量: {len(tools)}\n")
            continue
        
        if user_input.lower() == 'switch':
            USE_GROQ = not USE_GROQ
            if USE_GROQ:
                llm = Groq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)
                print("✅ 已切換到 Groq 雲端 API (更快)\n")
            else:
                llm = Ollama(model=CURRENT_MODEL, request_timeout=300.0)
                print(f"✅ 已切換到 Ollama 本地模型 ({CURRENT_MODEL})\n")
            Settings.llm = llm
            agent_worker = FunctionCallingAgentWorker.from_tools(tools, llm=llm, verbose=True)
            agent = AgentRunner(agent_worker)
            continue
        
        # Agent 執行任務
        print("\n🤖 Agent 分析中...\n")
        response = agent.chat(user_input)
        print(f"\n💬 Agent: {response}\n")
        
    except KeyboardInterrupt:
        print("\n\n👋 程式已中斷，再見！")
        break
    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}")
        print("💡 提示: 可以試試 'switch' 切換模型或重新提問\n")
