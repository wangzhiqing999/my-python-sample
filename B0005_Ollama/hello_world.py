import ollama

# 创建 Ollama 客户端实例
client = ollama.Client('hpt630:11434')

# 定义要使用的模型和输入的提示
model_name = "deepseek-r1:1.5b"
prompt = "你是谁"

try:
    # 调用 generate 方法生成文本
    response = client.generate(model_name, prompt)
    # 打印生成的文本
    print(response.response)
except Exception as e:
    print(f"发生错误: {e}")



