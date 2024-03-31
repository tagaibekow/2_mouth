from aiogram import Bot, Dispatcher, types, executor
from config import token
import logging
import sqlite3
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

conn = sqlite3.connect('test_drives.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS test_drives (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username INTEGER NOT NULL,
                    model TEXT NOT NULL,
                    date_time TEXT NOT NULL
                    );''')
conn.commit()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Здраствуйте, вас приветствует компания BMW", reply_markup=start_keyboard)

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    print(message)
    await message.answer(f"Здраствуйте, {message.from_user.full_name}! Чем могу вам помочь?")

start_buttons = [
    types.KeyboardButton("Модели автомобилей"),
    types.KeyboardButton("Цены"),
    types.KeyboardButton("Характеристики"),
    types.KeyboardButton("Специальные предложения")
]
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

model_button = [
    types.KeyboardButton('BMW IX M6'),
    types.KeyboardButton('BMW M5'),
    types.KeyboardButton('BMW M4'),
    types.KeyboardButton("Назад")
]

model_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*model_button)

@dp.message_handler(text="Модели автомобилей")
async def num_3(message: types.Message):
    await message.answer("Вот модели автомобилей", reply_markup=model_keyboard)

@dp.message_handler(text="BMW IX M6")
async def num_5(message: types.Message):
    await message.answer_photo('https://www.bmw.kg/content/dam/bmw/common/all-models/m-series/iX-60/2021/onepager/bmw-ix-m60-onepager-mc-performance-design-highlights-hero-desktop.jpg/jcr:content/renditions/cq5dam.resized.img.1680.large.time1636554778108.jpg')
    await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/bmw-ix-m60/2021/bmw-ix-m60-highlights/jcr:content/par/multicontent_1948771425/tabs/multicontenttab/items/smallteaser_92fb/image.transform/smallteaser/image.1659701303655.jpg')
    await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/bmw-ix-m60/2021/bmw-ix-m60-highlights/jcr:content/par/multicontent_1948771425/tabs/multicontenttab/items/smallteaser_807d/image.transform/smallteaser/image.1659701303694.jpg')
    await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/bmw-ix-m60/2021/bmw-ix-m60-highlights/jcr:content/par/multicontent_1948771425/tabs/multicontenttab/items/smallteaser_e652/image.transform/smallteaser/image.1659701303759.jpg')
    await message.answer_photo('https://www.bmw.kg/content/dam/bmw/common/all-models/m-series/iX-60/2021/onepager/bmw-ix-m60-onepager-ms-shytech-02.jpg/jcr:content/renditions/cq5dam.resized.img.585.low.time1636554826615.jpg')
    await message.answer_photo('https://www.bmw.kg/content/dam/bmw/common/all-models/m-series/iX-60/2021/onepager/bmw-ix-m60-onepager-gallery-impressions-thumbnail-09.jpg/jcr:content/renditions/cq5dam.resized.img.890.medium.time1707923935083.jpg')
    await message.answer_photo('https://www.bmw.kg/content/dam/bmw/common/all-models/m-series/iX-60/2021/onepager/bmw-ix-m60-onepager-gallery-impressions-thumbnail-02.jpg/jcr:content/renditions/cq5dam.resized.img.890.medium.time1634643882707.jpg')
    await message.answer_photo('https://www.bmw.kg/content/dam/bmw/common/all-models/m-series/iX-60/2021/onepager/bmw-ix-m60-onepager-gallery-impressions-thumbnail-05.jpg/jcr:content/renditions/cq5dam.resized.img.890.medium.time1707923934759.jpg')
    await message.answer_photo('https://www.bmw.kg/content/dam/bmw/common/all-models/m-series/iX-60/2021/onepager/bmw-ix-m60-onepager-gallery-impressions-thumbnail-06.jpg/jcr:content/renditions/cq5dam.resized.img.890.medium.time1640271472575.jpg')

@dp.message_handler(text="BMW M5")
async def num_6(message: types.Message):
    await message.answer('https://www.youtube.com/watch?v=qHQaLs1nypg')

@dp.message_handler(text="BMW M4")
async def num_7(message: types.Message):
    await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/m4-coupe/2022/bmw-4-series-coupe-m-automobiles-highlights/jcr:content/par/multicontent/tabs/multicontenttab_copy/items/smallteaser/image.transform/smallteaser/image.1672115152308.jpg')
    await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/m4-coupe/2022/bmw-4-series-coupe-m-automobiles-highlights/jcr:content/par/multicontent/tabs/multicontenttab_copy/items/smallteaser_copy/image.transform/smallteaser/image.1672115152361.jpg')
    await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/m4-coupe/2022/bmw-4-series-coupe-m-automobiles-highlights/jcr:content/par/multicontent/tabs/multicontenttab_copy/items/smallteaser_copy_cop/image.transform/smallteaser/image.1672115152431.jpg')
    await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/m4-coupe/2022/bmw-4-series-coupe-m-automobiles-highlights/jcr:content/par/multicontent/tabs/multicontenttab_1535450737/items/smallteaser_copy_cop/image.transform/smallteaser/image.1672115152943.jpg')
    await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/m4-coupe/2022/bmw-4-series-coupe-m-automobiles-highlights/jcr:content/par/multicontent/tabs/multicontenttab_1535450737/items/smallteaser/image.transform/smallteaser/image.1672115152894.jpg')
    await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/m4-coupe/2022/bmw-4-series-coupe-m-automobiles-highlights/jcr:content/par/multicontent/tabs/multicontenttab_249504282/items/smallteaser/image.transform/smallteaser/image.1672115152610.jpg')


bmw_button = [
    types.KeyboardButton('Цена BMW IX M6'),
    types.KeyboardButton('Цена BMW M5'),
    types.KeyboardButton('Цена BMW M4'),
    types.KeyboardButton("Назад")
]

bmw_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*bmw_button)

@dp.message_handler(text="Цены")
async def num_9(message: types.Message):
    await message.answer("Цены автомобилей", reply_markup=bmw_keyboard)

@dp.message_handler(text="Цена BMW IX M6")
async def num_01(message: types.Message):
    await message.answer("12 000 000 c")

@dp.message_handler(text="Цена BMW M5")
async def num_02(message: types.Message):
    await message.answer("5 580 000 c")

@dp.message_handler(text="Цена BMW M4")
async def num_03(message: types.Message):
    await message.answer("6 500 000 c")

@dp.message_handler(text='Назад')
async def rollback(message: types.Message):
    await start(message)

num01_button = [
    types.KeyboardButton('Характеристики BMW IX M6'),
    types.KeyboardButton('Характеристики BMW M5'),
    types.KeyboardButton('Характеристики BMW M4'),
    types.KeyboardButton("Назад")
]


num2_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*num01_button)

@dp.message_handler(text="Характеристики")
async def num_9(message: types.Message):
    await message.answer("Характеристики машин", reply_markup=num2_keyboard)

@dp.message_handler(text='Назад')
async def rollback(message: types.Message):
    await start(message)


@dp.message_handler(text='Характеристики BMW IX M6')
async def num_01(message: types.Message):
    await message.answer("""Мощность двигателя в кВт (л.с.):      455 (619)**\n

\nРазгон 0–100 км/ч в секундах:      3,8*

\nЗапас хода на электротяге (WLTP), км:      575*

\nКрутящий момент в Нм при 1/мин:      1 100***

\nЭнергопотребление в кВтч/100 км (WLTP):      21,6*

""")
    
@dp.message_handler(text="Характеристики BMW M5")
async def num_02(message: types.Message):
    await message.answer("""
 Мощность, л.с.:      460 (625)\n

Разгон 0–100 км/ч, с:      3.9\n

Расход топлива в смешанном цикле WLTP, л/100 км:      13.1–12.8\n

Выбросы CO2 в смешанном цикле WLTP, г/км:      296–288\n

""")

@dp.message_handler(text='Характеристики BMW M4')
async def num_03(message: types.Message):
    await message.answer("""
Мощность, кВт (л.с.) при об/мин:      405 (551)/6,250\n

\nМакс. крутящий момент, Нм при об/мин:      650/2,750-5,950

\nРазгон 0–100 км/ч в секундах:      3.7

\nРасход топлива в л/100 км (смешанный цикл):      10.1

""")

@dp.message_handler(text='Назад')
async def rollback(message: types.Message):
    await start(message)

num_button = [
    types.KeyboardButton('Гарантия 1+1'),
    types.KeyboardButton('Тест драйв'),  
    types.KeyboardButton("Назад")
]

num_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*num_button)

@dp.message_handler(text="Специальные предложения")
async def num(message: types.Message):
    await message.answer("Вот какие есть специальные предложения", reply_markup=num_keyboard)

@dp.message_handler(text="Гарантия 1+1")
async def num(message: types.Message):
    await message.answer("Мы дадим гарантию на 3 года")

test_buttons = [
    types.KeyboardButton('взять на тест BMW IX M6'),
    types.KeyboardButton('взять на тест BMW M5'),
    types.KeyboardButton('взять на тест BMW M4'),
    types.KeyboardButton("Назад")
]
test_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*test_buttons)

@dp.message_handler(text='Тест драйв')
async def test_drive(message: types.Message):
    await message.answer("Выберите модель для тест-драйва:", reply_markup=test_keyboard)

@dp.message_handler(text='взять на тест BMW IX M6')
async def test_car1(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    car_model = 'BMW IX M6'
    date_time = message.date.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO test_drives (username, model, date_time) VALUES (?, ?, ?)",
                   (username, car_model, date_time))
    conn.commit()

    await message.answer('Вы записались на тест-драйв BMW IX M6. Приходите к нам в офис в указанное время.')

@dp.message_handler(text='взять на тест BMW M5')
async def test_car1(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    car_model = 'BMW M5'
    date_time = message.date.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO test_drives (username, model, date_time) VALUES (?, ?, ?)",
                   (username, car_model, date_time))
    conn.commit()

    await message.answer('Вы записались на тест-драйв BMW M5. Приходите к нам в офис в указанное время.')

@dp.message_handler(text='взять на тест BMW M4')
async def test_car1(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    car_model = 'BMW M4'
    date_time = message.date.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO test_drives (username, model, date_time) VALUES (?, ?, ?)",
                   (username, car_model, date_time))
    conn.commit()

    await message.answer('Вы записались на тест-драйв BMW M4. Приходите к нам в офис в указанное время.')
    

executor.start_polling(dp, skip_updates=True)