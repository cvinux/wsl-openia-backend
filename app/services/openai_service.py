from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_openai(prompt: str) -> str:
    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )
    return response.output_text