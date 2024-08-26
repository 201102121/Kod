from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import logging

API_TOKEN = '' 

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


games = ["Minecraft", "Counter-Strike", "Hill Climb Racing", "MasterCraft"]

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [KeyboardButton(game) for game in games]
    keyboard.add(*buttons)
    
    await message.reply("Salom! O'yinlardan birini tanlang:", reply_markup=keyboard)

@dp.message_handler()
async def handle_message(message: types.Message):
    if message.text in games:
        await message.reply(f"Siz tanlagan o'yin: {message.text}")
    else:
        await message.reply("Iltimos, o'yinlardan birini tanlang.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
