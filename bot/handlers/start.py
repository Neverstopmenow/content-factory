from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards.main import main_keyboard

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я помогу тебе создавать контент с помощью AI.\n\n"
        "Выбери действие:",
        reply_markup=main_keyboard()
    )
