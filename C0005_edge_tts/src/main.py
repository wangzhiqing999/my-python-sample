import asyncio
import edge_tts

TEXT = "我的话讲完了！谁赞成？谁反对？"
VOICE = "zh-CN-YunyangNeural"
OUTPUT_FILE = "d:/test.mp3"

async def amain() -> None:
    """Main function"""
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)

if __name__ == "__main__":
    asyncio.run(amain())
