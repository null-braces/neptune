import openai
import time

from openai import OpenAI

from config import OPENAI_API_KEY, MODEL_NAME

openai.api_key = OPENAI_API_KEY

class LLMClient:
    def __init__(self, model=MODEL_NAME):
        self.model = model
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def chat(self, prompt, retries=3):
        for i in range(retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=prompt,
                )
                return response.choices[0].message.content
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(2 ** i)
        raise RuntimeError("LLM call failed after retries.")
