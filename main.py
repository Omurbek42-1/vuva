import asyncio
from distutils.cmd import Command
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv 
from os import getenv 
import logging


load_dotenv() 
bot=Bot(token=getenv("BOT_TOKEN"))
dp=Dispatcher() 


@dp.message() 
async def echo(message: types.Message):
    print("Message", message)
    print("User info", message.from_user.first_name)
    
    
    name = message.from_user.first_name
    await message.answer( 
        f"Привет,{name}"
    ) 
   
   
@dp.message(Command("picture"))
async def picture_handler(message: types.Message):
    file = types.FSInputFile(images/gnom.jpg)
    await message.answer_photo(photo=file, caption="Гномик")
    
    
async def main():
    await dp.start_polling(bot)
    
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())  
    
    
@dp.message() 
async def echo_handler(message: types.Message): 
    await message.reply(message.text)
    
    
