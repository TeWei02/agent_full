import os
import asyncio
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.tools import QueryEngineTool, ToolMetadata, FunctionTool
from llama_index.core.agent import ReActAgent
from llama_index.llms.ollama import Ollama
from llama_index.llms.groq import Groq
from llama_index.embeddings.ollama import OllamaEmbedding
import datetime
from typing import Optional

# ============================================
# 配置區
# ============================================
USE_GROQ = True  # True = 使用 Groq（快），False = 使用 Ollama（本地）
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")  # 填入你的 Groq API Key
OLLAMA_MODEL = "mistral:latest"  # 或 "llama3:latest", "mistral:latest"
PDF_FILE = "sample.pdf"  # 你要分析的 PDF

# ============================================
# 初始化
# ============================================
print("="*70)
print("🤖 ModernReader AI Agent - 完整版")
print("="*70 + "\n")

# 設定 LLM
if USE_GROQ:
    print("🌐 使用 Groq 雲端 API（速度快）...")
    os.environ["GROQ_API_KEY"] = GROQ_API_KEY
    llm = Groq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)
    embed_model = OllamaEmbedding(model_name="llama3:latest")  # Embedding 用本地
else:
    print(f"🖥️  使用本地 Ollama ({OLLAMA_MODEL})...")
    llm = Ollama(model=OLLAMA_MODEL, request_timeout=120.0)
    embed_model = OllamaEmbedding(model_name=OLLAMA_MODEL)

Settings.llm = llm
Settings.embed_model = embed_model
print("✅ LLM 已連接\n")

# 載入文件
print("📄 載入並索引文件...")
try:
    documents = SimpleDirectoryReader(input_files=[PDF_FILE]).load_data()
    index = VectorStoreIndex.from_documents(documents, show_progress=True)
    query_engine = index.as_query_engine(similarity_top_k=3)
    print(f"✅ 成功載入 {len(documents)} 個文件\n")
except Exception as e:
    print(f"❌ 載入失敗: {e}")
    print("提示: 確保 sample.pdf 存在於當前目錄\n")
    exit(1)

# ============================================
# 定義工具
# ============================================

# 工具 1: PDF 搜尋
pdf_tool = QueryEngineTool(
    query_engine=query_engine,
    metadata=ToolMetadata(
        name="search_pdf",
        description="搜尋並分析 PDF 文件內容，回答關於文件的問題。適用於查找資訊、理解內容、摘要重點。"
    ),
)

# 工具 2: 計算器
def calculate(expression: str) -> str:
    """
    執行數學計算
    
    Args:
        expression: 數學表達式，例如 "2+3*4" 或 "(100-25)/5"
    
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
    description="執行數學計算，支援 +, -, *, /, 括號等運算"
)

# 工具 3: 時間查詢
def get_time() -> str:
    """
    獲取當前時間和日期
    
    Returns:
        當前的完整日期時間
    """
    now = datetime.datetime.now()
    weekdays = ['週一', '週二', '週三', '週四', '週五', '週六', '週日']
    weekday = weekdays[now.weekday()]
    return f"當前時間: {now.strftime('%Y年%m月%d日')} {weekday} {now.strftime('%H:%M:%S')}"

time_tool = FunctionTool.from_defaults(
    fn=get_time,
    name="get_time",
    description="獲取當前的日期、時間和星期幾"
)

# 工具 4: 文件統計
def get_stats() -> str:
    """
    獲取文件的詳細統計資訊
    
    Returns:
        文件數量、字數等統計資料
    """
    total_chars = sum(len(doc.text) for doc in documents)
    total_words = sum(len(doc.text.split()) for doc in documents)
    avg_words = total_words // len(documents) if documents else 0
    
    return f"""📊 文件統計:
━━━━━━━━━━━━━━━━━━━━
📄 文件數量: {len(documents)} 個
📝 總字元數: {total_chars:,} 字元
🔤 總單字數: {total_words:,} 個
📈 平均字數: {avg_words:,} 字/文件
━━━━━━━━━━━━━━━━━━━━"""

stats_tool = FunctionTool.from_defaults(
    fn=get_stats,
    name="doc_stats",
    description="獲取載入文件的詳細統計資訊"
)

# 工具 5: ModernReader 功能介紹
def modernreader_info() -> str:
    """
    說明 ModernReader 系統的核心功能
    
    Returns:
        系統功能介紹
    """
    return """🚀 ModernReader 系統功能

━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 核心功能
━━━━━━━━━━━━━━━━━━━━━━━━━━

1. 多感官閱讀體驗 👁️👂✋
   • 視覺: 可調整字體、大小、顏色
   • 聽覺: AI 語音朗讀
   • 觸覺: 觸覺反饋輔助

2. AI 智能輔助 🤖
   • 內容摘要與重點提取
   • 智能問答系統
   • 個性化推薦

3. 無障礙設計 ♿
   • 視覺障礙者支援
   • 閱讀困難者輔助
   • 多語言支援

4. 技術架構 ⚙️
   • LlamaIndex RAG 系統
   • LlamaParse 文件解析
   • Ollama/Groq LLM
   • 向量資料庫檢索

━━━━━━━━━━━━━━━━━━━━━━━━━━"""

features_tool = FunctionTool.from_defaults(
    fn=modernreader_info,
    name="modernreader_info",
    description="說明 ModernReader 系統的完整功能和架構"
)

# 工具 6: 網路搜尋（模擬）
def web_search(query: str) -> str:
    """
    模擬網路搜尋功能
    
    Args:
        query: 搜尋查詢
    
    Returns:
        搜尋結果
    """
    return f"[模擬搜尋] 關於 '{query}' 的搜尋結果：此功能需要整合真實搜尋 API（如 Google, Bing）"

search_tool = FunctionTool.from_defaults(
    fn=web_search,
    name="web_search",
    description="在網路上搜尋資訊（目前為模擬功能）"
)

# 整合所有工具
tools = [pdf_tool, calculator_tool, time_tool, stats_tool, features_tool, search_tool]

# ============================================
# 建立 Agent
# ============================================
print("⚙️  建立 ReAct Agent...")

agent = ReActAgent(
    name="ModernReader_Agent",
    description="ModernReader 的智能助手，可以分析文件、回答問題、執行計算等多種任務",
    tools=tools,
    llm=llm,
    verbose=False,  # 改成 False 減少日誌輸出
    timeout=120.0,  # 2分鐘超時
)

print("✅ Agent 已啟動\n")

# ============================================
# 自動測試
# ============================================
async def auto_test():
    """自動測試 Agent 功能"""
    print("="*70)
    print("🧪 自動測試 Agent 能力")
    print("="*70 + "\n")
    
    tests = [
        ("時間查詢", "現在幾點？"),
        ("數學計算", "計算 (15 + 25) * 3"),
        ("文件統計", "這個文件有多少字？"),
        ("系統功能", "ModernReader 有哪些功能？"),
        ("內容分析", "這個 PDF 主要講什麼？簡短回答"),
        ("組合任務", "現在幾點？然後告訴我文件字數")
    ]
    
    for i, (category, test) in enumerate(tests, 1):
        print(f"\n{'='*70}")
        print(f"📝 測試 {i}/{len(tests)} - [{category}]")
        print(f"問題: {test}")
        print('='*70)
        
        try:
            result = await agent.run(user_msg=test)
            print(f"✅ 回答: {result}\n")
        except Exception as e:
            print(f"❌ 錯誤: {e}\n")

# ============================================
# 互動模式
# ============================================
async def interactive_mode():
    """互動式對話模式"""
    print("\n" + "="*70)
    print("💬 進入 Agent 互動模式")
    print("="*70)
    print("\n🔧 Agent 能力:")
    print("  📄 search_pdf      - 搜尋並分析 PDF 內容")
    print("  🧮 calculator      - 執行數學計算")
    print("  ⏰ get_time        - 查詢當前時間")
    print("  📊 doc_stats       - 獲取文件統計")
    print("  💡 modernreader    - 系統功能說明")
    print("  🌐 web_search      - 網路搜尋（模擬）")
    
    print("\n📋 特殊指令:")
    print("  'help'    - 顯示幫助")
    print("  'tools'   - 列出所有工具")
    print("  'switch'  - 切換 LLM（Groq ↔ Ollama）")
    print("  'info'    - 顯示當前配置")
    print("  'clear'   - 清除螢幕")
    print("  'exit'    - 退出程式")
    
    print("\n💡 提示: Agent 會自動選擇合適的工具來回答你的問題")
    print("="*70 + "\n")
    
    chat_history = []
    
    while True:
        try:
            user_input = input("你: ").strip()
            
            if not user_input:
                continue
            
            # 處理特殊指令
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("\n👋 感謝使用 ModernReader AI Agent！再見~")
                break
            
            if user_input.lower() == 'help':
                print("\n📖 幫助資訊:")
                print("  - 直接輸入問題，Agent 會自動處理")
                print("  - 可以問關於 PDF 內容的問題")
                print("  - 可以要求執行計算")
                print("  - 可以查詢時間和統計資訊")
                print("  - 可以問 ModernReader 的功能\n")
                continue
            
            if user_input.lower() == 'tools':
                print("\n🔧 可用工具清單:\n")
                for i, tool in enumerate(tools, 1):
                    print(f"{i}. {tool.metadata.name}")
                    print(f"   📝 {tool.metadata.description}\n")
                continue
            
            if user_input.lower() == 'info':
                llm_type = "Groq (雲端)" if USE_GROQ else f"Ollama (本地 - {OLLAMA_MODEL})"
                print(f"\n📊 當前配置:")
                print(f"  🤖 LLM: {llm_type}")
                print(f"  📄 文件: {PDF_FILE}")
                print(f"  📚 文件數: {len(documents)}")
                print(f"  🔧 工具數: {len(tools)}\n")
                continue
            
            if user_input.lower() == 'clear':
                os.system('clear' if os.name == 'posix' else 'cls')
                continue
            
            if user_input.lower() == 'switch':
                print("\n⚠️  切換 LLM 需要重新啟動程式")
                print("請修改程式開頭的 USE_GROQ 設定\n")
                continue
            
            # 正常查詢
            print("\n🤖 Agent 思考中...\n")
            
            try:
                result = await agent.run(user_msg=user_input)
                print(f"💬 Agent: {result}\n")
                
                # 記錄對話歷史
                chat_history.append({"user": user_input, "agent": str(result)})
                
            except asyncio.TimeoutError:
                print("⏱️  查詢超時，請嘗試簡化問題或切換到更快的模型\n")
            except Exception as e:
                print(f"❌ 執行錯誤: {e}")
                print("💡 提示: 可以嘗試重新表述問題\n")
        
        except KeyboardInterrupt:
            print("\n\n👋 程式已中斷，再見！")
            break
        except Exception as e:
            print(f"\n❌ 未預期的錯誤: {e}\n")

# ============================================
# 主函數
# ============================================
async def main():
    """主程式入口"""
    # 執行自動測試
    await auto_test()
    
    # 進入互動模式
    await interactive_mode()

# ============================================
# 執行程式
# ============================================
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 程式已終止")
    except Exception as e:
        print(f"\n❌ 程式錯誤: {e}")

