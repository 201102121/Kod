from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import subprocess

# API tokeningizni shu yerga kiriting
API_TOKEN = ''

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Salom! Kod yozing va men sizga natijani ko\'rsataman.')

async def execute_code(update: Update, context: CallbackContext) -> None:
    user_code = update.message.text
    try:
        # Kodni bajarish va natijani olish
        result = subprocess.run(
            ['python', '-c', user_code],
            capture_output=True,
            text=True
        )
        if result.stderr:
            response = f"Xatolik:\n{result.stderr}"
        else:
            response = f"Natija:\n{result.stdout}"
    except Exception as e:
        response = f"Xatolik: {e}"
    
    await update.message.reply_text(response)

def main() -> None:
    application = Application.builder().token(API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, execute_code))

    application.run_polling()

if __name__ == '__main__':
    main()
