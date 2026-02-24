from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from agents.content_agent import ContentAgent

router = Router()
agent = ContentAgent()


class ContentForm(StatesGroup):
    waiting_for_topic = State()
    waiting_for_style = State()


@router.message(F.text == "Создать контент")
async def request_topic(message: Message, state: FSMContext):
    await message.answer("Введи тему для контента:")
    await state.set_state(ContentForm.waiting_for_topic)


@router.message(ContentForm.waiting_for_topic)
async def generate_content(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Генерирую контент...")
    result = await agent.generate(topic=message.text)
    await message.answer(result)
