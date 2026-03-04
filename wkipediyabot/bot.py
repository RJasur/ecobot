import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

# Tokenni qoyadigan joy
API_TOKEN = "API_TOKEN"
bot = Bot(token=API_TOKEN)

# Dispatcher yaratish
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    """/start komandasi uchun"""
    await message.answer("Salom!\nMen yangi eco  botiman!")

@dp.message(Command("help"))
async def command_help_handler(message: Message):
    """/help komandasi uchun"""
    await message.reply("Sizga qanday yordam kerak?")

@dp.message()
async def echo_handler(message: Message):
    """Barcha xabarlarni qaytaruvchi (Echo) funksiya"""
    try:
        # Xabarni qaytarish
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # Agar xabar turi kutilmagan bo'lsa
        await message.answer("Tushunarsiz xabar...")

async def main():
    bot = Bot(token=API_TOKEN)
    # Botni ishga tushirish
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    asyncio.run(main())
