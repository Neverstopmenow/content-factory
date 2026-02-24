import anthropic

from config.settings import settings
from agents.prompts.templates import CONTENT_PROMPT


class ContentAgent:
    def __init__(self):
        self.client = anthropic.AsyncAnthropic(api_key=settings.anthropic_api_key)

    async def generate(self, topic: str, style: str = "engaging") -> str:
        response = await self.client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=CONTENT_PROMPT,
            messages=[
                {"role": "user", "content": f"Тема: {topic}\nСтиль: {style}"},
            ]
        )
        return response.content[0].text
