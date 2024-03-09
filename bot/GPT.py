import config as cfg
import openai
from openai import OpenAI
client = OpenAI(
    api_key=cfg._GPTTOKEN_,
)
def askGPT(texttoansw: str): # Нет возможности проверить, но должно работать. Токен заблокирован без впн, количество использований закончилось.
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Ты - бот-помошник для сотрудников компании Ростелеком, занимающейся подключением клиентов к интернету и прочими штуками. Ответь в шутливой манере на следующий текст: " + texttoansw,    
                }
            ],
            model="gpt-3.5-turbo",
        )
        anstosend = chat_completion.choices[0].message.content
        return anstosend
    except Exception as e:
        print(e)
        return e