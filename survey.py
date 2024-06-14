from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


survey_router = Router() 


# FSM - Finite state  Mashine - Конечный автомат 
class Booksurvey(StatesGroup); 
    name = State() # имя пользователя 
    age = State() # возраст 
    gender = State() # пол 
    genre = State() # любимый жанр 


@survey_router.message(Command("opros"))
async def start_survey(message: types.Message, state: FSMContext):
     # устанавливаем состояние 
    await.state.set_state(Booksurvey.name)
    await message.answer("Как вас зовут?")
    
    
@survey_router.message(Booksurvey.age) 
async def process_name(message: types.Message, state: FSMContext): 
    # устанавливаем состояние 
    await state.set_state(Booksurvey.name)
    await message.answer("Сколько вам лет?") 
    
      
@survey_router.message(Booksurvey.gender) 
async def process_gender(message: types.Message, state: FSMContext): 
    # устанавливаем состояние 
    await state.set_state(Booksurvey.gender)
    await message.answer("Какого вы пола?")  
    
        
@survey_router.message(Booksurvey.genre) 
async def process_name(message: types.Message, state: FSMContext): 
    # устанавливаем состояние 
    await state.set_state(Booksurvey.genre)
    await message.answer("Ваш любимый жанр?")  
    
          
@survey_router.message(Booksurvey.name) 
async def process_name(message: types.Message, state: FSMContext): 
    # устанавливаем состояние 
    await state.set_state(Booksurvey.name)
    await message.answer("Спасибо за прохождение опроса")  
    
    
    from aiogram import Bot, Dispatcher, types, executor
    

bot = Bot(token="YOUR_API_TOKEN")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Оставить отзыв")
    keyboard.add(button)
    await message.answer("Добро пожаловать!", reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
