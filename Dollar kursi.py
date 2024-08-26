import asyncio
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# O'zingizning bot tokeningizni kiriting
bot = Bot(token="")
dp = Dispatcher()

# Free Forex API URL
api_url = 'https://bank.uz/uz/currency/dollar-ssha'

def get_dollar_exchange_rate():
    try:
        response = requests.get(api_url)
        data = response.json()
        # USD/UZS valyuta juftligini olish
        exchange_rate = data['rates']['USDUZS']['rate']
        return exchange_rate
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        return None

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    exchange_rate = get_dollar_exchange_rate()
    if exchange_rate:
        response_text = f"Dollar kursi: 1 USD = {exchange_rate} UZS"
    else:
        response_text = "Dollar kursini olishda xatolik yuz berdi. Iltimos, keyinroq qaytadan urinib ko'ring."
    
    await message.answer(response_text)

async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

if __name__ == '__main__':
    asyncio.run(main())
