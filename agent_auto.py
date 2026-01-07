import os
import asyncio
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.tools import QueryEngineTool, ToolMetadata, FunctionTool
from llama_index.core.agent import ReActAgent
from llama_index.llms.groq import Groq
from llama_index.embeddings.ollama import OllamaEmbedding
import datetime
from typing import List, Dict

# ============================================
# 配置
# ============================================
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
PDF_FILE = "sample.pdf"

# ============================================
# Agent 設置
# ============================================
print("🤖 初始化 AI Agent...")

os.environ["GROQ_API_KEY"] = GROQ_API_KEY
llm = Groq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)
Settings.llm = llm
Settings.embed_model = OllamaEmbedding(model_name="llama3:latest")

# 載入文件
documents = SimpleDirectoryReader(input_files=[PDF_FILE]).load_data()
index = VectorStoreIndex.from_documents(documents, show_progress=False)
query_engine = index.as_query_engine(similarity_top_k=3)

# ============================================
# 定義工具（簡化版）
# ============================================
pdf_tool = QueryEngineTool(
    query_engine=query_engine,
    metadata=ToolMetadata(name="search_pdf", description="搜尋PDF內容")
)

def calculate(expr: str) -> str:
    try: return f"{expr} = {eval(expr)}"
    except: return "計算錯誤"

def get_time() -> str:
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_stats() -> str:
    return f"文件: {len(documents)}個, 字數: {sum(len(d.text.split()) for d in documents)}"

def execute_command(command: str) -> str:
    """執行系統命令"""
    import subprocess
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
        return result.stdout or result.stderr
    except Exception as e:
        return f"執行失敗: {e}"

def read_file(filepath: str) -> str:
    """讀取文件內容"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()[:1000]  # 限制1000字元
    except Exception as e:
        return f"讀取失敗: {e}"

def write_file(filepath: str, content: str) -> str:
    """寫入文件"""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"✅ 已寫入 {filepath}"
    except Exception as e:
        return f"寫入失敗: {e}"

# 註冊工具
tools = [
    pdf_tool,
    FunctionTool.from_defaults(fn=calculate, name="calc", description="計算"),
    FunctionTool.from_defaults(fn=get_time, name="time", description="時間"),
    FunctionTool.from_defaults(fn=get_stats, name="stats", description="統計"),
    FunctionTool.from_defaults(fn=execute_command, name="exec", description="執行命令"),
    FunctionTool.from_defaults(fn=read_file, name="read", description="讀文件"),
    FunctionTool.from_defaults(fn=write_file, name="write", description="寫文件"),
]

# 建立 Agent
agent = ReActAgent(
    name="AutoAgent",
    tools=tools,
    llm=llm,
    verbose=False
)

print("✅ Agent 已啟動\n")

# ============================================
# 自動任務系統
# ============================================
class TaskManager:
    """自動任務管理器"""
    
    def __init__(self, agent):
        self.agent = agent
        self.tasks: List[Dict] = []
        self.completed: List[Dict] = []
    
    def add_task(self, name: str, description: str, priority: int = 1):
        """添加任務"""
        self.tasks.append({
            "name": name,
            "description": description,
            "priority": priority,
            "status": "pending"
        })
        self.tasks.sort(key=lambda x: x["priority"], reverse=True)
    
    async def execute_task(self, task: Dict):
        """執行單個任務"""
        print(f"\n🔄 執行任務: {task['name']}")
        print(f"📝 描述: {task['description']}")
        
        try:
            result = await self.agent.run(user_msg=task['description'])
            task['status'] = 'completed'
            task['result'] = str(result)
            self.completed.append(task)
            print(f"✅ 完成: {result}\n")
            return result
        except Exception as e:
            task['status'] = 'failed'
            task['error'] = str(e)
            print(f"❌ 失敗: {e}\n")
            return None
    
    async def run_all(self):
        """執行所有任務"""
        print(f"🚀 開始執行 {len(self.tasks)} 個任務\n")
        
        for task in self.tasks:
            await self.execute_task(task)
            await asyncio.sleep(1)  # 避免 API 限速
        
        print(f"\n✅ 所有任務完成！")
        print(f"   成功: {len([t for t in self.completed if t['status']=='completed'])}")
        print(f"   失敗: {len([t for t in self.tasks if t.get('status')=='failed'])}")
    
    def report(self):
        """生成報告"""
        report = "# 任務執行報告\n\n"
        for task in self.completed:
            report += f"## {task['name']}\n"
            report += f"- 狀態: {task['status']}\n"
            report += f"- 結果: {task.get('result', 'N/A')}\n\n"
        
        with open("task_report.md", "w", encoding="utf-8") as f:
            f.write(report)
        
        print("📄 報告已儲存至 task_report.md")

# ============================================
# 預定義任務清單
# ============================================
async def demo_auto_tasks():
    """示範自動任務"""
    
    tm = TaskManager(agent)
    
    # 添加任務
    tm.add_task("早安檢查", "現在幾點？今天星期幾？", priority=3)
    tm.add_task("文件分析", "分析 PDF 文件，給我重點摘要", priority=2)
    tm.add_task("數據統計", "告訴我文件的詳細統計資訊", priority=2)
    tm.add_task("技術評估", "ModernReader 使用了哪些技術？", priority=1)
    tm.add_task("計算測試", "計算 (100 + 200) * 3", priority=1)
    
    # 執行所有任務
    await tm.run_all()
    
    # 生成報告
    tm.report()

# ============================================
# 智能助手模式
# ============================================
async def smart_assistant():
    """智能助手 - 主動提供幫助"""
    
    print("="*70)
    print("🤖 智能助手模式")
    print("="*70)
    print("\n我會主動幫你完成任務，像 Comet 一樣！\n")
    
    # 開場分析
    print("📊 讓我先分析一下當前環境...\n")
    
    current_time = get_time()
    doc_stats = get_stats()
    
    print(f"⏰ 當前時間: {current_time}")
    print(f"📄 {doc_stats}")
    
    # 自動建議
    hour = datetime.datetime.now().hour
    
    if 6 <= hour < 12:
        print("\n💡 早安！今天要分析什麼文件嗎？")
    elif 12 <= hour < 18:
        print("\n💡 午安！需要我幫忙整理文件摘要嗎？")
    else:
        print("\n💡 晚安！要不要我幫你生成今天的工作報告？")
    
    # 互動模式
    print("\n" + "="*70)
    print("輸入任務，我會自動執行（輸入 'auto' 進入全自動模式）")
    print("="*70 + "\n")
    
    while True:
        try:
            user_input = input("你: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['exit', 'quit']:
                print("\n👋 再見！")
                break
            
            if user_input.lower() == 'auto':
                print("\n🚀 進入全自動模式...\n")
                await demo_auto_tasks()
                continue
            
            # 執行任務
            print(f"\n🤖 收到任務，開始執行...\n")
            result = await agent.run(user_msg=user_input)
            print(f"✅ 完成: {result}\n")
            
            # 主動建議下一步
            print("💡 還需要我做什麼嗎？")
            
        except KeyboardInterrupt:
            print("\n\n👋 已中斷")
            break
        except Exception as e:
            print(f"\n❌ 錯誤: {e}\n")

# ============================================
# 主程式
# ============================================
async def main():
    """主函數"""
    
    print("選擇模式:")
    print("1. 全自動任務模式（Demo）")
    print("2. 智能助手模式（互動）")
    
    choice = input("\n請選擇 (1/2): ").strip()
    
    if choice == '1':
        await demo_auto_tasks()
    else:
        await smart_assistant()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 程式已終止")

