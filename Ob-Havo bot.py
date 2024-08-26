import asyncio
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot(token="")
dp = Dispatcher()


api_key = ''


cities = ["Toshkent", "Andijon", "Farg'ona", "Samarkand", "Buxoro", "Nukus",
    "Namangan", "Qashqadaryo", "Sirdaryo", "Jizzax", "Surxondaryo", "Xorazm",
    "Karakalpakstan"]


def create_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=2)
    buttons = [ReplyKeyboardMarkup(text=cities, callback_data=cities) for cities in regions]
    keyboard.add(*buttons)
    return keyboard


@dp.message(CommandStart())
async def start_cmd(message: types.Message):

    city_list = "\n".join(cities)
    response_text = (
        'Botga xush kelibsiz! Shahar nomini yuboring va ob-havo ma’lumotlarini oling.\n'
        'Quyidagi shaharlardan birini tanlashingiz mumkin:\n' + city_list
    )
    await message.answer(response_text)

@dp.message()
async def get_weather(message: types.Message):
    city_name = message.text
    limit = 1
    try:
   
        city_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={api_key}'
        response = requests.get(city_url).json()
        
        if not response:
            await message.answer("Shahar topilmadi. Iltimos, qaytadan urinib ko'ring.")
            return
        
        lon = response[0]['lon']
        lat = response[0]['lat']

        
        weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}'
        weather_response = requests.get(weather_url).json()

        weather = weather_response['main']['temp']
        description = weather_response['weather'][0]['description']
        
        await message.answer(f"{city_name} shahridagi ob-havo: {weather}°C, {description.capitalize()}")

    except Exception as e:
        await message.answer("Ob-havo ma'lumotlarini olishda xatolik yuz berdi. Iltimos, keyinroq qaytadan urinib ko'ring.")
        print(f"Xatolik: {e}")

async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

if __name__ == '__main__':
    asyncio.run(main())

import asyncio
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
\
bot = Bot(token="7379804789:AAFCLh4IuLi5C5LOonaAdUTxzrmggP33p4I")
dp = Dispatcher()

api_key = 'b4a9ef7543307ec65db0227a0b308d4b'

regions = [
    "Toshkent", "Andijon", "Farg'ona", "Samarkand", "Buxoro", "Nukus",
    "Namangan", "Qashqadaryo", "Sirdaryo", "Jizzax", "Surxondaryo", "Xorazm",
    "Karakalpakstan"
]


def create_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = [KeyboardButton(cities) for cities in regions]
    keyboard.add(*buttons)
    return keyboard

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    keyboard = create_keyboard()
    response_text = (
        'Botga xush kelibsiz! Shahar nomini yuboring va ob-havo ma’lumotlarini oling.\n'
        'Quyidagi viloyatlardan birini tanlashingiz mumkin:'
    )
    await message.answer(response_text, reply_markup=keyboard)

@dp.message()
async def get_weather(message: types.Message):
    city_name = message.text
    limit = 1
    try:
        
        city_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={api_key}'
        response = requests.get(city_url).json()
        
        if not response:
            await message.answer("Shahar topilmadi. Iltimos, qaytadan urinib ko'ring.")
            return
        
        lon = response[0]['lon']
        lat = response[0]['lat']

       
        weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}'
        weather_response = requests.get(weather_url).json()

        
        weather = weather_response['main']['temp']
        description = weather_response['weather'][0]['description']
        
       
        await message.answer(f"{city_name} shahridagi ob-havo: {weather}°C, {description.capitalize()}")

    except Exception as e:
        await message.answer("Ob-havo ma'lumotlarini olishda xatolik yuz berdi. Iltimos, keyinroq qaytadan urinib ko'ring.")
        print(f"Xatolik: {e}")
    

async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

if __name__ == '__main__':
    asyncio.run(main())