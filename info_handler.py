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
    

def address(update, context):
    update.message.reply_text("Наш адрес: улица Пушкина, дом Колотушкина.")
    
def contacts(update, context):
    update.message.reply_text("Наши контактные данные: телефон: +1234567890, email: info@restaurant.com.")
    
def about(update, context):
    update.message.reply_text("Небольшое описание нашего заведения: рассказываем о том, что мы лучшие в городе и т.д.")
    
def website(update, context):
    update.message.reply_text("Наш веб-сайт: www.restaurant.com.")
    
def instagram(update, context):
    update.message.reply_text("Наш Instagram профиль: @restaurant_official.")
