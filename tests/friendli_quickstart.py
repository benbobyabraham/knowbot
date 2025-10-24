import os
from openai import OpenAI

client = OpenAI(
    api_key="flp_3bfdY1iVb9wY6Wr9lzWcxHSWtDck28bGyZ5oB7R58kd0db",
    base_url="https://api.friendli.ai/dedicated/v1",
)

chat_completion = client.chat.completions.create(
    model="dep433mjmg4eoe6",
    messages=[
        {
            "role": "user",
            "content": "Tell me how to make a delicious pancake"
        }
    ]
)
print(chat_completion.choices[0].message.content)