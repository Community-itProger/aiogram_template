from aiogram.dispatcher.filters import CommandStart
from loader import dp
from aiogram.types import Message


@dp.message_handler(CommandStart())
async def command_start(message: Message):
    await message.answer(
        text=f"Привет! Это готовый шаблон aiogram-бота от @itproger_admin"
    )