import os
from openai import OpenAI

def get_ai_response(message):
  
    client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=os.getenv("HF_TOKEN"),
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b:cerebras",
        messages=[{"role": "user", "content": message}],
        max_completion_tokens=int(os.getenv('MAX_TOKENS'))
    )

    return response.choices[0].message.content