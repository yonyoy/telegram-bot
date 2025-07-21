# file: telegram_bot.py

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, filters
)
import os

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Replace with your actual bot token or set via environment variable
BOT_TOKEN = os.getenv('7659830956:AAG5AVCKyp8zGgCBSm9OinzTMmJsykn8s9E', '7659830956:AAG5AVCKyp8zGgCBSm9OinzTMmJsykn8s9E')

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = {
        'username': 'demo_user123',
        'password': 'securePass!@#'
    }

    welcome_text = (
        "👋 សួស្តីបង! 🎉\n"
        "🧑‍💻 បងបានចុះឈ្មោះរួចរាល់ហើយ!\n"
        "🆔 នេះគឺជា អ្នកប្រើប្រាស់ និង លេខសម្ងាត់ សម្រាប់ចូលលេង៖\n"
        f"👤 អ្នកប្រើប្រាស់៖ {data['username']}\n"
        f"🔑 លេខសម្ងាត់៖ {data['password']}\n"
        "🎮 ចូលលេងហ្គេម៖ https://ubet789kh.com/\n"
        "📲 ប្រសិនបើមានសំណួរឬបញ្ហា សូមទាក់ទង Admin៖\n"
        "🔹 Telegram៖ https://t.me/UB789bot\n"
        "🔹 Facebook៖ https://facebook.com/ub789page\n"
        "🙏 សូមអរគុណចំពោះការជឿទុកចិត្តរបស់បង!\n"
        "— — — — — — — — — — — —\n"
        "👋 Hello brother/sister! 🎉\n"
        "🧑‍💻 Your registration is complete!\n"
        f"🆔 Username: {data['username']}\n"
        f"🔑 Password: {data['password']}\n"
        "🎮 Play here: https://ubet789kh.com/\n"
        "📲 If you have any questions, contact Admin:\n"
        "🔹 Telegram: https://t.me/UB789bot\n"
        "🔹 Facebook: https://facebook.com/ub789page\n"
        "🙏 Thank you so much for your trust!"
    )

    keyboard = [
        [InlineKeyboardButton("🎮 ចូលលេងហ្គេម", url="https://ubet789kh.com/")],
        [InlineKeyboardButton("📲 Telegram Admin", url="https://t.me/UB789bot")],
        [InlineKeyboardButton("🌐 Facebook Page", url="https://facebook.com/ub789page")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# Message handler: reply to any text
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text
    await update.message.reply_text(f"អ្នកបានបញ្ចូល៖ {user_text}")

# Main function to run the bot
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()

if __name__ == '__main__':
    main()
