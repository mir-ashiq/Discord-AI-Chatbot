import openai
import os
from dotenv import load_dotenv # python-dotenv

load_dotenv()
openai.api_key = os.getenv('CHATANYWHERE_KEY')
openai.api_base = "https://api.chatanywhere.com.cn/v1"
def printurl():
    # response = openai.Image.create(
    #     prompt="a cute anime girl doing",
    #     n=1,
    #     size="256x256"
    # )
    print()
printurl()
