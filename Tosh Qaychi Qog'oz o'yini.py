import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random

API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)

games = {}

# Emoji tanlovlari
rock_emoji = '✊'
scissors_emoji = '✌️'
paper_emoji = '✋'
choices = {rock_emoji: 'Tosh', scissors_emoji: 'Qaychi', paper_emoji: 'Qog\'oz'}

# Tugmalar yaratish uchun funksiya
def create_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton(rock_emoji), KeyboardButton(scissors_emoji), KeyboardButton(paper_emoji))
    return markup

# O'yinni boshlash va xabarlarni boshqarish
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Bu 'Tosh, Qaychi, Qog'oz' o'yini botidir. O'yinni boshlash uchun /play yoki robotga qarshi o'ynash uchun /robot buyrug'ini yozing.")

@bot.message_handler(commands=['play'])
def start_game(message):
    chat_id = message.chat.id
    games[chat_id] = {'mode': '2p', 'player1': None, 'player2': None}
    bot.send_message(chat_id, "O'yin boshlandi! Birinchi o'yinchi, tanlovingizni qiling:", reply_markup=create_markup())

@bot.message_handler(commands=['robot'])
def play_against_robot(message):
    chat_id = message.chat.id
    games[chat_id] = {'mode': 'robot', 'player1': None, 'robot': None}
    bot.send_message(chat_id, "Siz robotga qarshi o'ynayapsiz! Tanlovingizni qiling:", reply_markup=create_markup())

@bot.message_handler(func=lambda message: message.text in choices.keys())
def handle_choice(message):
    chat_id = message.chat.id
    if chat_id in games:
        game = games[chat_id]
        choice = choices[message.text]
        
        if game['mode'] == '2p':
            if game['player1'] is None:
                game['player1'] = choice
                bot.send_message(chat_id, "Ikkinchi o'yinchi, tanlovingizni qiling:", reply_markup=create_markup())
            elif game['player2'] is None:
                game['player2'] = choice
                determine_winner(chat_id)
        elif game['mode'] == 'robot':
            if game['player1'] is None:
                game['player1'] = choice
                game['robot'] = random.choice(list(choices.values()))
                robot_emoji = [k for k, v in choices.items() if v == game['robot']][0]  # Robotning emojisini topish
                bot.send_message(chat_id, f"Robot {robot_emoji} tanladi.")
                determine_winner(chat_id)
    else:
        bot.send_message(chat_id, "O'yinni boshlash uchun /play yoki /robot buyrug'ini yozing.")

def determine_winner(chat_id):
    game = games[chat_id]
    player1 = game['player1']
    player2 = game['player2'] if game['mode'] == '2p' else game['robot']

    if player1 == player2:
        result = "Durang!"
    elif (player1 == 'Tosh' and player2 == 'Qaychi') or (player1 == 'Qaychi' and player2 == 'Qog\'oz') or (player1 == 'Qog\'oz' and player2 == 'Tosh'):
        result = "O'yinchi 1 g'olib bo'ldi!"
    else:
        result = "O'yinchi 2 g'olib bo'ldi!" if game['mode'] == '2p' else "Robot g'olib bo'ldi!"

    bot.send_message(chat_id, f"O'yinchi 1: {player1}\nO'yinchi 2: {player2 if game['mode'] == '2p' else 'Robot'}\n\n{result}")
    del games[chat_id]

# Botni ishga tushirish
bot.polling()
