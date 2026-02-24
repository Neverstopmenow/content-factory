import anthropic

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from config.settings import settings

router = Router()

# История сообщений на пользователя
user_histories: dict[int, list] = {}


@router.message(F.text == "Чат с AI")
async def start_chat(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_histories[user_id] = []
    await message.answer(
        "Привет! Я Claude — AI ассистент. Задай любой вопрос.\n\n"
        "Для выхода напиши /stop"
    )
    await state.set_state("chat")


@router.message(F.text == "/stop")
async def stop_chat(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Чат завершён.", reply_markup=None)


@router.message(F.state == "chat")
async def handle_chat(message: Message, state: FSMContext):
    user_id = message.from_user.id

    if user_id not in user_histories:
        user_histories[user_id] = []

    user_histories[user_id].append({
        "role": "user",
        "content": message.text
    })

    # Ограничиваем историю до 20 сообщений
    if len(user_histories[user_id]) > 20:
        user_histories[user_id] = user_histories[user_id][-20:]

    await message.answer("Думаю...")

    client = anthropic.AsyncAnthropic(api_key=settings.anthropic_api_key)
    response = await client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="Ты — умный AI ассистент. Отвечай чётко и по делу на русском языке.",
        messages=user_histories[user_id]
    )

    reply = response.content[0].text

    user_histories[user_id].append({
        "role": "assistant",
        "content": reply
    })

    await message.answer(reply)
