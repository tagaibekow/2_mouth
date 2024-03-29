import re
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from config import token
import logging, sqlite3

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

connection = sqlite3.connect('logistics.db'),
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id INT,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    phone VARCHAR(100),
    age INTEGER
);""")

start_buttons = [
    types.KeyboardButton('Регистрация'),
    types.KeyboardButton('Шаблон регистрации')
]
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

def validate_phone(phone):
    return re.match(r'^\+\d{11}$', phone) is not None

def validate_age(age):
    try:
        return int(age) >= 14
    except ValueError:
        return False

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer("""Привет! Я чат-бот карго компании Geeks Express.

Данный бот поможет вам получить персональный код и правильно заполнить адрес склада в Китае 🇨🇳

С Уважением команда Geeks Express :)
""", reply_markup=start_keyboard)
    
@dp.message_handler(text="Шаблон регистрации")
async def shablon_register(message: types.Message):
    await message.reply("""Для регистрации в нашей карго компании вам нужно:
1) Укажите свое имя
2) Укажите свою фамилию
3) Укажите рабочий номер телефона 
в международном формате +996777223344
4) Укажите ваш возраст
И вы автоматически получите код клиента :D
""")

class RegisterState(StatesGroup):
    first_name = State()
    last_name = State()
    phone = State()
    age = State()

@dp.message_handler(text="Регистрация")
async def start_register(message: types.Message):
    await message.answer(f"{message.from_user.full_name}, давайте начнем регистрацию")
    await message.answer("Введите имя:")
    await RegisterState.first_name.set()

@dp.message_handler(state=RegisterState.first_name)
async def get_user_lastname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text
    await message.answer("Введите фамилию:")
    await RegisterState.next()

@dp.message_handler(state=RegisterState.last_name)
async def get_user_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text
    await message.answer("Введите свой номер:")
    await RegisterState.next()

@dp.message_handler(state=RegisterState.phone)
async def get_user_age(message:types.Message, state:FSMContext):
    phone_pattern = re.compile(r'^\+\d{12}$')
    if not phone_pattern.match(message.text):
        await message.answer("Неверный формат номера. Введите номер в формате +996XXXXXXXXX")
        return
    await state.update_data(phone=message.text)
    await message.answer("Введите возраст:")
    await RegisterState.age.set()

@dp.message_handler(state=RegisterState.age)
async def end_register_user(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    if not validate_age(data['age']):
        await message.answer("Извините, регистрация доступна только для лиц старше 14 лет.")
        return
    
    user_data = await state.get_data()
    cursor.execute("INSERT INTO users (id, first_name, last_name, phone, age) VALUES (?, ?, ?, ?, ?)",
                   (message.from_user.id, user_data['first_name'], user_data['last_name'], user_data['phone'], user_data['age']))
    connection.commit()
    
    await message.answer("Спасибо, вы успешно зарегистрированы!")

    await state.finish()

@dp.message_handler()
async def not_found(message: types.Message):
    await message.answer("Я вас не понял, введите /start")

executor.start_polling(dp, skip_updates=True)
