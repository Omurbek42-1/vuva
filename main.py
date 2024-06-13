from telegram.ext import Updater
from handlers.menu_handler import setup_handlers as setup_menu_handlers
from handlers.random_dish_handler import setup_handlers as setup_random_dish_handlers

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Устанавливаем обработчики из разных модулей
    setup_menu_handlers(dispatcher)
    setup_random_dish_handlers(dispatcher)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
