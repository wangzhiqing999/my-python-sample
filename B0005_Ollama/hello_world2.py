import ollama

# 创建 Ollama 客户端实例
client = ollama.Client('hpt630:11434')

# 定义要使用的模型和输入的提示
model_name = "deepseek-r1:1.5b"
prompt = "给我介绍一下 Python 语言。"

try:
    # 以流式方式生成文本
    for part in client.generate(model_name, prompt, stream=True):
        print(part.response, end="", flush=True)
    print()
except Exception as e:
    print(f"发生错误: {e}")
