import aiosqlite
from database.queries import Queries

class Database:
    def __init__(self, path):
        self.path = path

    async def create_tables(self):
        async with aiosqlite.connect(self.path) as conn:
            # создание всех таблиц
            await conn.execute(Queries.CREATE_SURVEY_TABLE)
            await conn.execute(Queries.DROP_GENRES_TABLE)
            await conn.execute(Queries.DROP_BOOKS_TABLE)
            await conn.execute(Queries.CREATE_GENRES_TABLE)
            await conn.execute(Queries.CREATE_BOOKS_TABLE)
            await conn.execute(Queries.POPULATE_GENRES)
            await conn.execute(Queries.POPULATE_BOOKS)
            # здесь может быть создание других таблиц
            # которые нам нужны
            await conn.commit()

    async def execute(self, query, params: tuple = ()):
        async with aiosqlite.connect(self.path) as conn:
            await conn.execute(query,params)
            await conn.commit()
            
            
            import sqlite3

class Database:
    def __init__(self, db_name='reviews.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                review TEXT,
                rating INTEGER,
                date_posted TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def insert_review(self, user_id, review, rating):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO reviews (user_id, review, rating) VALUES (?, ?, ?)
        ''', (user_id, review, rating))
        self.conn.commit()

    def close(self):
        self.conn.close()

# Пример использования:
if __name__ == '__main__':
    db = Database()
    db.close()

import telebot
from database import Database
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)
db = Database()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Отправь мне свой отзыв.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Предположим, что бот ожидает от пользователя текст отзыва и оценку
    user_id = message.from_user.id
    review_text = message.text
    rating = 5  # Пусть будет всегда максимальная оценка для примера
    db.insert_review(user_id, review_text, rating)
    bot.reply_to(message, "Спасибо за ваш отзыв!")

bot.polling()
