import telebot
import random

API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)

class TicTacToe:
    def __init__(self, robot=False):
        self.board = [' '] * 9  # 3x3 maydon (bo'sh joylar)
        self.current_player = "X"
        self.winner = None
        self.game_over = False
        self.robot = robot

    def print_board(self):
        return (f"{self.board[0]} | {self.board[1]} | {self.board[2]}\n"
                f"--+---+--\n"
                f"{self.board[3]} | {self.board[4]} | {self.board[5]}\n"
                f"--+---+--\n"
                f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
                self.game_over = True
            elif ' ' not in self.board:
                self.game_over = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.robot and self.current_player == "O" and not self.game_over:
                    self.robot_move()
        else:
            return False
        return True

    def robot_move(self):
        empty_positions = [i for i, x in enumerate(self.board) if x == ' ']
        position = random.choice(empty_positions)
        self.make_move(position)

    def check_winner(self):
        win_conditions = [
            [0, 1, 2, 3], [3, 4, 5], [6, 7, 8],  # Gorizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertikal
            [0, 4, 8], [2, 4, 6]             # Diagonal
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return True
        return False

# O'yinni boshlash va xabarlarni boshqarish
games = {}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Bu X va O (tic-tac-toe) o'yini botidir. O'yinni boshlash uchun /play yoki robotga qarshi o'ynash uchun /robot buyrug'ini yozing.")

@bot.message_handler(commands=['play'])
def play_game(message):
    chat_id = message.chat.id
    games[chat_id] = TicTacToe()
    bot.send_message(chat_id, "O'yin boshlandi!\n" + games[chat_id].print_board())
    bot.send_message(chat_id, "Iltimos, joylashuvni tanlang (0-8):")

@bot.message_handler(commands=['robot'])
def play_against_robot(message):
    chat_id = message.chat.id
    games[chat_id] = TicTacToe(robot=True)
    bot.send_message(chat_id, "Siz robotga qarshi o'ynayapsiz!\n" + games[chat_id].print_board())
    bot.send_message(chat_id, "Iltimos, joylashuvni tanlang (0-8):")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    if chat_id in games:
        game = games[chat_id]
        try:
            position = int(message.text)
            if 0 <= position <= 8:
                if game.make_move(position):
                    bot.send_message(chat_id, game.print_board())
                    if game.game_over:
                        if game.winner:
                            bot.send_message(chat_id, f"O'yin tugadi! {game.winner} g'olib bo'ldi!")
                        else:
                            bot.send_message(chat_id, "O'yin tugadi! Durang!")
                        del games[chat_id]
                    elif game.robot and game.current_player == "O":
                        bot.send_message(chat_id, "Robot harakat qilyapti...")
                        bot.send_message(chat_id, game.print_board())
                        if game.game_over:
                            if game.winner:
                                bot.send_message(chat_id, f"O'yin tugadi! {game.winner} g'olib bo'ldi!")
                            else:
                                bot.send_message(chat_id, "O'yin tugadi! Durang!")
                            del games[chat_id]
                        else:
                            bot.send_message(chat_id, f"Navbat: {game.current_player}")
                else:
                    bot.send_message(chat_id, "Bu joy band! Boshqa joy tanlang.")
            else:
                bot.send_message(chat_id, "Noto'g'ri joylashuv. Iltimos, 0 dan 8 gacha bo'lgan raqamni kiriting.")
        except ValueError:
            bot.send_message(chat_id, "Noto'g'ri kirish. Iltimos, raqam kiriting.")
    else:
        bot.send_message(chat_id, "O'yinni boshlash uchun /play yoki /robot buyrug'ini yozing.")

# Botni ishga tushirish
bot.polling()
