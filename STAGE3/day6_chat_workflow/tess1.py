from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("MIMO_API_KEY"),
    base_url="https://api.xiaomimimo.com/v1"
)

response = client.chat.completions.create(
    model="mimo-v2.5-pro",
    messages=[
        {
            "role": "user",
            "content": "Halo"
        }
    ]
)

print(response.choices[0].message.content)