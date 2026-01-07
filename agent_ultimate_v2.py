import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.llms.groq import Groq
from llama_index.embeddings.ollama import OllamaEmbedding

print("🚀 ModernReader 終極免費 AI Agent 啟動中...\n")

# ============ 配置選項 ============
USE_GROQ = True  # True = 使用 Groq（快），False = 使用 Ollama（本地）
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")  # 填入你的 Groq Key

# ============ 設定 LLM ============
if USE_GROQ:
    print("🌐 使用 Groq 雲端 API（速度快）...")
    os.environ["GROQ_API_KEY"] = GROQ_API_KEY
    llm = Groq(
        model="llama-3.3-70b-versatile",
        api_key=GROQ_API_KEY
    )
    Settings.llm = llm
    print("✅ Groq LLM 已連接\n")
else:
    print("🖥️  使用本地 Ollama（完全免費）...")
    llm = Ollama(
        model="llama3:latest",  # 使用你已有的模型
        request_timeout=120.0
    )
    Settings.llm = llm
    print("✅ Ollama 已連接\n")

# ============ 設定 Embedding（用 Ollama，不需要額外套件）============
print("📊 載入 Ollama Embedding 模型...")
Settings.embed_model = OllamaEmbedding(
    model_name="llama3:latest",  # 使用你已有的模型做 embedding
    base_url="http://localhost:11434"
)
print("✅ Embedding 已準備\n")

# ============ 載入 PDF ============
print("📄 載入 PDF 文件...")
try:
    documents = SimpleDirectoryReader(
        input_files=["sample.pdf"]
    ).load_data()
    print(f"✅ 成功載入 {len(documents)} 個文件")
    print(f"   總字數: {sum(len(doc.text) for doc in documents)} 字\n")
except Exception as e:
    print(f"❌ 載入失敗: {e}\n")
    exit(1)

# ============ 建立向量索引 ============
print("🔍 建立向量索引（這可能需要一點時間）...")
try:
    index = VectorStoreIndex.from_documents(documents, show_progress=True)
    print("✅ 索引建立完成\n")
except Exception as e:
    print(f"❌ 索引建立失敗: {e}\n")
    exit(1)

# ============ 建立查詢引擎 ============
print("⚙️  設置查詢引擎...")
query_engine = index.as_query_engine(
    similarity_top_k=3,
    streaming=False
)
print("✅ 查詢引擎已準備\n")

# ============ 自動測試 ============
print("="*60)
print("🎯 AI Agent 已準備好！開始自動測試")
print("="*60 + "\n")

test_queries = [
    "這個文件主要講什麼？請用繁體中文回答",
    "文件中提到哪些技術？",
]

for i, query in enumerate(test_queries, 1):
    print(f"📝 測試 {i}/{len(test_queries)}: {query}")
    try:
        response = query_engine.query(query)
        print(f"🤖 回答: {response}\n")
    except Exception as e:
        print(f"❌ 查詢失敗: {e}\n")

# ============ 互動模式 ============
print("="*60)
print("💬 進入互動模式")
print("="*60)
print("指令:")
print("  - 輸入問題：直接提問")
print("  - 'models': 顯示可用的 Ollama 模型")
print("  - 'use <model>': 切換模型 (例如: use mistral:latest)")
print("  - 'switch': 切換 Groq/Ollama")
print("  - 'info': 顯示當前配置")
print("  - 'exit': 退出\n")

current_model = "llama3:latest"

while True:
    try:
        user_input = input("你: ").strip()
        
        if not user_input:
            continue
            
        if user_input.lower() in ['exit', 'quit', 'q']:
            print("\n👋 感謝使用 ModernReader AI Agent！再見~")
            break
        
        if user_input.lower() == 'models':
            print("\n📦 你已下載的模型:")
            print("  - llama3:latest (4.7 GB)")
            print("  - llama2:latest (3.8 GB)")
            print("  - mistral:latest (4.4 GB)")
            print("  - phi:latest (1.6 GB)")
            print("  - phi3:latest (2.2 GB)")
            print(f"\n當前使用: {current_model}\n")
            continue
        
        if user_input.lower().startswith('use '):
            new_model = user_input[4:].strip()
            try:
                Settings.llm = Ollama(model=new_model, request_timeout=120.0)
                Settings.embed_model = OllamaEmbedding(model_name=new_model)
                query_engine = index.as_query_engine(similarity_top_k=3)
                current_model = new_model
                print(f"✅ 已切換到 {new_model}\n")
            except Exception as e:
                print(f"❌ 切換失敗: {e}\n")
            continue
        
        if user_input.lower() == 'switch':
            USE_GROQ = not USE_GROQ
            if USE_GROQ:
                Settings.llm = Groq(model="llama-3.1-70b-versatile", api_key=GROQ_API_KEY)
                print("✅ 已切換到 Groq（雲端）\n")
            else:
                Settings.llm = Ollama(model=current_model, request_timeout=120.0)
                print(f"✅ 已切換到 Ollama (本地 - {current_model})\n")
            query_engine = index.as_query_engine(similarity_top_k=3)
            continue
        
        if user_input.lower() == 'info':
            llm_type = "Groq (雲端)" if USE_GROQ else f"Ollama (本地 - {current_model})"
            print(f"\n📊 當前配置:")
            print(f"   LLM: {llm_type}")
            print(f"   Embedding: Ollama ({current_model})")
            print(f"   文件數: {len(documents)}")
            print(f"   總字數: {sum(len(doc.text) for doc in documents)}\n")
            continue
        
        # 正常查詢
        print("🤖 思考中...")
        response = query_engine.query(user_input)
        print(f"\n{response}\n")
        
    except KeyboardInterrupt:
        print("\n\n👋 已中斷，再見！")
        break
    except Exception as e:
        print(f"❌ 錯誤: {e}\n")
        print("提示: 如果是 Groq API 錯誤，試試輸入 'switch' 切換到 Ollama\n")

