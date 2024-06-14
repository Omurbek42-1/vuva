from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start(update, context):
    buttons = [
        [InlineKeyboardButton("Наше меню", callback_data='menu')],
        [InlineKeyboardButton("Отзывы", callback_data='reviews')],
        [InlineKeyboardButton("Наши вакансии", callback_data='vacancies')]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text("Выберите интересующий раздел:", reply_markup=reply_markup)
