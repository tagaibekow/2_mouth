from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import sqlite3, time, random, logging

from config import token

bot = Bot(token)
storege = MemoryStorage()
dp = Dispatcher(bot, storage=storege)
logging.basicConfig(level=logging.INFO)

conn = sqlite3.connect('kino_bot.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username VARCHAR(50),
        age INT, 
        city VARCHAR(50),
        balance REAL DEFAULT 0
    )
''')
conn.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS seats (
        id INTEGER PRIMARY KEY,
        row_number INTEGER,
        seat_number INTEGER,
        status TEXT DEFAULT 'available'
    )
''')
conn.commit()

# def add_seats():
#     rows = 4  
#     seats_per_row = 10  

#     for row_number in range(1, rows + 1):
#         for seat_number in range(1, seats_per_row + 1):
#             cursor.execute('INSERT INTO seats (row_number, seat_number) VALUES (?, ?)', (row_number, seat_number))
#     conn.commit()


# add_seats()

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Зарегистрироватся')).add(KeyboardButton('/info'))

@dp.message_handler(commands=['start', 'go'])
async def cmd_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}', reply_markup=start_keyboard)

class UserState(StatesGroup):
    name = State()
    age = State()
    city = State()

@dp.message_handler(text='Зарегистрироватся')
async def cmd_register(message: types.Message):
    user_id = message.from_user.id
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    existing_user = cursor.fetchone()
    if existing_user:
        await message.answer("Вы уже зарегистрированы.")
    else:
        await message.answer("Введите ваше имя:")
        await UserState.name.set()

@dp.message_handler(state=UserState.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer("Введите ваш возраст:")
    await UserState.next()

@dp.message_handler(state=UserState.age)
async def process_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await message.answer("Введите ваш город:")
    await UserState.next()

@dp.message_handler(state=UserState.city)
async def process_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
        cursor.execute('INSERT INTO users (user_id, username, age, city) VALUES (?, ?, ?, ?)',
                       (message.from_user.id, data['name'], data['age'], data['city']))
        conn.commit()
    await state.finish()
    await message.answer("Регистрация завершена. Спасибо!")
    
class DepositState(StatesGroup):
    amount = State()

@dp.message_handler(commands=['balance'])
async def cmd_balance(message: types.Message):
    await message.answer('Введите сумму для паполнение')
    await DepositState.amount.set()
    
@dp.message_handler(state=DepositState.amount)
async def cmd_amount(message: types.Message, state: FSMContext): 
    user_id = message.from_user.id
    cursor.execute('SELECT balance FROM users WHERE user_id = ?', (user_id,))
    balance = cursor.fetchone()
    
    try: 
        amount = float(message.text)
        if amount <= 0:
            raise ValueError('сумма должна быть положительной')
        
        cursor.execute('UPDATE users SET balance = balance + ? WHERE user_id = ? ', (amount, user_id))
        conn.commit()
        
        await message.reply(f'Баланс успешно паполнен {amount}')
        await state.finish()
    except ValueError as e: 
        await message.answer(f'Ошибка {e}')   
        await state.finish()
        
class TicketPurchase(StatesGroup):
    Row = State()
    Seat = State()
        
@dp.message_handler(commands='shop_tokens')
async def cmd_shop(message: types.Message):
    await message.answer('Выберите место ')
    await TicketPurchase.Row.set()
    
@dp.message_handler(state=TicketPurchase.Row)
async def cmd_row(message: types.Message, state: FSMContext):
    row = message.text
    await state.update_data(row=row)
    await message.answer("Выберите место:")
    await TicketPurchase.Seat.set
    
@dp.message_handler(state=TicketPurchase.Seat)
async def process_seat(message: types.Message, state: FSMContext):
    seat = message.text
    data = await state.get_data()
    row = data.get('row')
    user_id = message.from_user.id


    cursor.execute('SELECT status FROM seats WHERE row_number = ? AND seat_number = ?', (row, seat))
    seat_status = cursor.fetchone()
    if seat_status and seat_status[0] == 'available':
 
        await message.answer(f"Вы выбрали место: Ряд {row}, Место {seat}")
        
        cursor.execute('UPDATE seats SET status = "occupied" WHERE row_number = ? AND seat_number = ?', (row, seat))
        conn.commit()

        cursor.execute('SELECT username, city FROM users WHERE user_id = ?', (user_id,))
        user_data = cursor.fetchone()
        first_name = user_data[0]
        city = user_data[1]
       
        await message.answer("Билет успешно куплен!")
        await state.finish()
    else:
       
        await message.answer(f"Извините, место {seat} в ряду {row} уже занято. Выберите другое место.")
        await state.finish()
        
executor.start_polling(dp, skip_updates=True)