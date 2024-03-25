from aiogram import Bot, Dispatcher, types, executor
from config import token
import logging

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

start_buttons = [
    types.KeyboardButton('Помощь'),
    types.KeyboardButton('Курсы'),
    types.KeyboardButton('О нас'), 
    types.KeyboardButton('Пробные уроки'),
    types.KeyboardButton('Мероприятие'),
    types.KeyboardButton('Адрес')
]
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    print(message)
    await message.answer('Привет, на связи Geeks! Чем могу помочь?', reply_markup=start_keyboard)
    
@dp.message_handler(text='Помощь')
async def help(message:types.Message):
    await message.reply(f"{message.from_user.full_name} напишите о своей проблеме")
    
@dp.message_handler(text='О нас')
async def about_us(message:types.Message):
    await message.answer("Geeks - это it курсы в Бишкеке, Кара-Балте, Оше и Ташкенте с 2018 года")
    
@dp.message_handler(text='Адрес')
async def address(message:types.Message):
    await message.answer("Ош - Мырзалы Аматова 1Б (БЦ Томирис)")
    await message.answer_location(40.5194, 72.803)
    
courses_buttons = [
    types.KeyboardButton('Backend'),
    types.KeyboardButton('Frontend'),
    types.KeyboardButton('Android'), 
    types.KeyboardButton('UX/UI'),
    types.KeyboardButton('Назад'),
]
courses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*courses_buttons)

@dp.message_handler(text="Курсы")
async def all_courses(message:types.Message):
    await message.answer("Вот все наши курсы:", reply_markup=courses_keyboard)
    
@dp.message_handler(text="Назад")
async def back(message:types.Message):
    await start(message)
    
@dp.message_handler(text="Backend")
async def backend(message:types.Message):
    await message.answer("Backend - это северная сторона сайта или приложение \nМесяц обучение: 5 месяцев\nСтоимость 10000 сом в месяц  ")
    
@dp.message_handler(text="Frontend")
async def backend(message:types.Message):
    await message.answer("Frontend - презентационная часть web приложений, информационной или программной системы, её пользовательский интерфейс и связанные с ним компоненты; применяется в соотношении с базисной частью системы, её внутренней реализацией, называемой в этом случае бэкендом\nМесяц обучение: 5 месяцев\nСтоимость 10000 сом в месяц  ")
    
@dp.message_handler(text="Android")
async def backend(message:types.Message):
    await message.answer("Android - операционная система, которая открыта для всех: разработчиков, дизайнеров и производителей устройств. Это означает, что возможность экспериментировать, предлагать революционные идеи и воплощать их в жизнь доступна большому количеству людей.\nМесяц обучение: 7 месяцев\nСтоимость 10000 сом в месяц  ")
    
@dp.message_handler(text="UX/UI")
async def backend(message:types.Message):
    await message.answer("UI ― это user interface, пользовательский интерфейс, проще говоря ― оформление сайта: сочетания цветов, шрифты, иконки и кнопки. UX ― это функционал интерфейса, UI ― его внешний вид. В современном дизайне UX и UI практически всегда идут рядом, потому что они очень тесно связаны\nМесяц обучение: 3 месяцев\nСтоимость 10000 сом в месяц  ")
    
@dp.message_handler(text="Мероприятие")
async def backend(message:types.Message):
    await message.answer("""ПРИГЛАШАЕМ 23 МАРТА НА “IT-НООРУЗ В ОШЕ” 🚀\n

Впервые в Оше Geeks проводит ВЕСЕННЮЮ ЯРМАРКУ ІТ-ПРОФЕССИЙ, 🌸\n

Вас ждут:\n
\n▫16 пробных уроков по Backend, Frontend, Мобильная разработка, UX/Ul-дизайн
\n▫️Гарантированные призы
\n▫️Праздничный фуршет
\n▫️Скидки от 50% до 100%

\nУчастие БЕСПЛАТНОЕ 🙌🏻""")
    
@dp.message_handler(text="Пробные уроки")
async def backend(message:types.Message):
    await message.answer("""🔥БЕСПЛАТНЫЕ ПРОБНЫЕ УРОКИ В GEEKS👇🏻\n

\n▫️ПОНЕДЕЛЬНИК
\n- 10:00 - Детское программирование
\n- 15:00 - Детское программирование

\n▫️ВТОРНИК
\n- 15:00 - UX/UI дизайн

\n▫️СРЕДА
\n- 10:00 - Детское программирование
\n- 15:00 - Детское программирование
\n- 19:00 - Frontend разработка

\n▫️ЧЕТВЕРГ
\n- 16:00 - Backend разработка

\n▫️ПЯТНИЦА
\n- 17:00 - UX/UI дизайн

\n▫️СУББОТА
\n- 16:00 - отбор на GeeksPro
\n- 17:00 - UX/UI дизайн

\n❗️Чтобы записаться или узнать подробную информацию о
\nнаших курсах оставляйте ➕ в комментариях⬇️
___
\nДля связи с нами:
\n📞0557 05 2018
\n📞0777 05 2018
\n📞0507 05 2018
\n📍 Адрес:
\nг. Ош, ул. Мырзалы Аматова, 15 стр, БЦ «Томирис»
\n⏳График работы:
\nКаждый день с 09:00 до 21:00""")

@dp.message_handler()
async def about_us(message:types.Message):
    await message.reply("я вас не понял")

executor.start_polling(dp)