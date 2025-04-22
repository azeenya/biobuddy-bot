from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

import os

TOKEN = os.environ['7952404034:AAER0lPpzmA5Osj4QMDPHXa1_b0zvt95RRw']  # Токен будет браться из переменных окружения

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Напиши /snack, чтобы выбрать перекус!")

async def snack(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Сладкое", callback_data='sweet')],
        [InlineKeyboardButton("Солёное", callback_data='salty')],
        [InlineKeyboardButton("Сытное", callback_data='filling')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выбери тип перекуса:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'sweet':
        await query.edit_message_text(text="Альтернатива сладкому:\n1. Финики с орехами\n2. Тёмный шоколад\n3. Йогурт с мёдом")
    elif query.data == 'salty':
        await query.edit_message_text(text="Солёный перекус:\n1. Хумус с морковью\n2. Сыр с хлебцами\n3. Оливки")
    elif query.data == 'filling':
        await query.edit_message_text(text="Сытный перекус:\n1. Яйцо с авокадо\n2. Бутерброд с тунцом\n3. Каша с орехами")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("snack", snack))
    app.add_handler(CallbackQueryHandler(button))
    print("Бот запущен!")
    app.run_polling()
