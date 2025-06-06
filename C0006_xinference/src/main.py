from xinference.client import Client

TEXT = "我的话讲完了！谁赞成？谁反对？"
OUTPUT_FILE = "d:/test_output.mp3"

def txt2mp3(input_text, output_file) :
    """ 文本内容， 生成 mp3 文件. """
    client = Client("http://192.168.1.33:9998")

    # 列出 Xinference 中正在运行的模型
    print(client.list_models())

    # 这里是启动模型， 如果是已经启动的话，就没必要运行这一句了。
    # model_uid = client.launch_model(model_name="ChatTTS", model_type="audio")

    model = client.get_model("ChatTTS")

    # 文字转语音.
    audio_data = model.speech(
        input= input_text,
        voice="echo",
        stream= False)

    # print(audio_data)

    # 二进制数据写入文件.
    with open(output_file, "wb") as f:
        f.write(audio_data)


if __name__ == "__main__":
    txt2mp3(TEXT, OUTPUT_FILE)
