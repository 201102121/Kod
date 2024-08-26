import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
    
# O'zingizning bot tokeningizni kiriting
API_TOKEN = ''
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Maktab dars jadvali ma'lumotlari
# Ushbu jadval misol sifatida kiritilgan, haqiqiy jadvalni o'z ehtiyojingizga moslashtiring
schedule = {
    "7-B": {
        "Duyshanba": "Matematika, Fizika, Ingliz tili, Kimyo",
        "Seyshanba": "Biologiya, Tarix, Informatika, Dasturlash",
        "Chorshanba": "Matematika, Geografiya, O'zbek tili, Fizika",
        "Payshanba": "Ingliz tili, Kimyo, Tarix, Sport",
        "Juma": "Matematika, Informatika, Biologiya, Tasviriy San'at",
        "Shanba": "Ochiq kun",
        "Yakshanba": "Ochiq kun"
    },
    "8-B": {
        "Duyshanba": "Matematika, Fizika, Ingliz tili, Kimyo",
        "Seyshanba": "Biologiya, Tarix, Informatika, Dasturlash",
        "Chorshanba": "Matematika, Geografiya, O'zbek tili, Fizika",
        "Payshanba": "Ingliz tili, Kimyo, Tarix, Sport",
        "Juma": "Matematika, Informatika, Biologiya, San'at",
        "Shanba": "Ochiq kun",
        "Yakshanba": "Ochiq kun"
    },
    
    
}

def create_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = [KeyboardButton("Jadvalni ko'rsatish"), KeyboardButton("Jadvalni yangilash")]
    keyboard.add(*buttons)
    return keyboard

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    response_text = "Salom! Sizning maktab dars jadvalingizni ko'rsatish uchun 'Jadvalni ko'rsatish' tugmasini bosing."
    await message.answer(response_text, reply_markup=create_keyboard())

@dp.message()
async def handle_message(message: types.Message):
    if message.text.lower() == "jadvalni ko'rsatish":
        user_id = str(message.from_user.id)
        if user_id in schedule:
            user_schedule = schedule[user_id]
            schedule_text = "\n".join(f"{day}: {classes}" for day, classes in user_schedule.items())
            response_text = f"Sizning dars jadvalingiz:\n{schedule_text}"
        else:
            response_text = "Jadval topilmadi. Iltimos, botni yangilab ko'ring yoki ma'lumotni to'g'rilash uchun admin bilan bog'laning."
        await message.answer(response_text)

    elif message.text.lower() == "jadvalni yangilash":
        # Bu qism jadvalni yangilash imkoniyatlarini qo'shish uchun joy. Misol uchun, ma'lumotlarni fayldan yoki ma'lumotlar bazasidan olish mumkin.
        await message.answer("Jadvalni yangilash funksiyasi qo'shilmagan.")

async def main():
    try:
        print("Bot ishga tushmoqda...")
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

if __name__ == '__main__':
    asyncio.run(main())
