from openai import AsyncOpenAI

from config.settings import settings
from agents.prompts.templates import CONTENT_PROMPT


class ContentAgent:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)

    async def generate(self, topic: str, style: str = "engaging") -> str:
        response = await self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": CONTENT_PROMPT},
                {"role": "user", "content": f"Тема: {topic}\nСтиль: {style}"},
            ]
        )
        return response.choices[0].message.content
