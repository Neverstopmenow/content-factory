from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Создать контент")],
            [KeyboardButton(text="История"), KeyboardButton(text="Настройки")],
        ],
        resize_keyboard=True
    )
