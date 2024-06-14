from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start(update, context):
    buttons = [
        [InlineKeyboardButton("Наше меню", callback_data='menu')],
        [InlineKeyboardButton("Отзывы", callback_data='reviews')],
        [InlineKeyboardButton("Наши вакансии", callback_data='vacancies')],
        [InlineKeyboardButton("Наш адрес", callback_data='address')],
        [InlineKeyboardButton("Контакты", callback_data='contacts')],
        [InlineKeyboardButton("О нас", callback_data='about')],
        [InlineKeyboardButton("Наш сайт", callback_data='website')],
        [InlineKeyboardButton("Инстаграм профиль", callback_data='instagram')]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text("Выберите интересующий раздел:", reply_markup=reply_markup)
