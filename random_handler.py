from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from models.menu import get_random_dish

def random_dish(update, context):
    dish = get_random_dish()
    update.message.reply_photo(dish.photo, caption=dish.name)
