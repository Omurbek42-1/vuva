from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from models.menu import get_random_dish

def show_menu(update, context):
    buttons = [
        [InlineKeyboardButton("Показать случайное блюдо", callback_data='random_dish')]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text("Выберите действие:", reply_markup=reply_markup)

def random_dish(update, context):
    dish = get_random_dish()
    update.message.reply_photo(dish.photo, caption=dish.name)
