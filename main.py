import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config.settings import settings
from bot.handlers import start, content, settings as settings_handler, chat

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=settings.telegram_bot_token)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(start.router)
    dp.include_router(content.router)
    dp.include_router(chat.router)
    dp.include_router(settings_handler.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
