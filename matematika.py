import telebot


API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men matematik amallarni bajaruvchi botman. Qo'shish, ayirish, ko'paytirish yoki bo'lish amallarini bajarish uchun ifodani kiriting. Masalan: '2 + 2', '5 * 3', '10 / 2', yoki '7 - 4'.")


def calculate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Xato: {e}"


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    expression = message.text
    result = calculate_expression(expression)
    bot.reply_to(message, f"Natija: {result}")


bot.polling()
