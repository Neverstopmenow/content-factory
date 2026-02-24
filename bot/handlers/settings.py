from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text == "Настройки")
async def show_settings(message: Message):
    await message.answer("Настройки пока в разработке.")
