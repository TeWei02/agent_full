from llama_parse import LlamaParse
import os

# 設定 API key
os.environ["LLAMA_CLOUD_API_KEY"] = "llx-AvRJnVizVUCa5HEjmoxeX36BvT6NythHlPioAlhkHoLmcWTp"

# 初始化 parser
parser = LlamaParse(
    result_type="markdown",
    verbose=True
)

# 測試解析
try:
    documents = parser.load_data("test.pdf")
    print(f"成功解析！共 {len(documents)} 個文件")
    print(documents[0].text[:200])  # 顯示前 200 字
except Exception as e:
    print(f"錯誤: {e}")

