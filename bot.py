
import os
import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties

TOKEN = os.getenv("API_TOKEN")

dp = Dispatcher()
router = Router()
dp.include_router(router)

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("👋 Привет! Я работаю на Render 24/7.")

async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
