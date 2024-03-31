from aiogram import Bot, Dispatcher, types, executor
from config import token
import logging

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

main_menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu_keyboard.add(
    types.KeyboardButton("Места где можно поесть"),
    types.KeyboardButton("Достопримечательности"),
    types.KeyboardButton("Оставить отзыв")
)
back_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

@dp.message_handler(text="Достопримечательности")
async def samsa(message:types.Message):
    await message.answer("Вы выбрали Достопримечательности!", reply_markup=landmarks_keyboard)

landmarks_buttons = [
    types.KeyboardButton('Пик-Ленина'),
    types.KeyboardButton('Кыргыз-Ата'),
    types.KeyboardButton('Водопад Абшир-Ата'),
    types.KeyboardButton('Алай'),
    types.KeyboardButton('гора Сулайман-Тоо'),
    types.KeyboardButton('Назад')
]
landmarks_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*landmarks_buttons)

@dp.message_handler(text="Пик-Ленина")
async def samsa(message:types.Message):
    await message.answer("Вы выбрали Пик-Ленина!", reply_markup=lenina_keyboard)
    
lenina_buttons = [
    types.KeyboardButton('Фотография'),
    types.KeyboardButton('Туры'),
    types.KeyboardButton('Информация'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('Назад')
]
lenina_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*lenina_buttons)

@dp.message_handler(text="Фотография")
async def photo(message:types.Message):
    await message.answer_photo('')
    await message.answer_photo('')
    await message.answer_photo('')
    await message.answer_photo('')
    
@dp.message_handler(text="Туры")
async def tury(message:types.Message):
    await message.answer()
   
    
@dp.message_handler(text='Информация')
async def information(message:types.Message):
    await message.answer('')
    
@dp.message_handler(text='Адрес')
async def your(message:types.Message):
    await message.answer('')
    await message.answer_location('')























cafes_buttons = [
    types.KeyboardButton('Samsa Land'),
    types.KeyboardButton('Царский Двор'),
    types.KeyboardButton('Ожак Кебаб'),
    types.KeyboardButton('Маленькая Япония'),
    types.KeyboardButton('Суши тайм'),
    types.KeyboardButton('Назад1')
]
cafes_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*cafes_buttons)

@dp.message_handler(text="Samsa Land")
async def samsa(message:types.Message):
    await message.answer("Кафе Samsa Land приветствует вас!", reply_markup=samsa_keyboard)
    
samsa_buttons = [
    types.KeyboardButton('Фотография'),
    types.KeyboardButton('Видео'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Назад')
]
samsa_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*samsa_buttons)

@dp.message_handler(text="Фотография")
async def photo(message:types.Message):
    await message.answer_photo('')
    await message.answer_photo('')
    await message.answer_photo('')
    await message.answer_photo('')
    
# @dp.message_handler(text="Видео")
# async def video(message:types.Message):
#     await message.answer_video('c:\\Users\\Welcome\\Pictures\\Saved Pictures\\ED4F4FDF1D726A2540C874F5E0B215AA_video_dashinit.mp4')
#     await message.answer_video('c:\\Users\\Welcome\\Pictures\\Saved Pictures\\0F44E0E452ED7B0CA540CD23C44D5EB1_video_dashinit.mp4')
    
@dp.message_handler(text='Адрес')
async def address(message:types.Message):
    await message.answer('HR22+3F3, Ош')
    await message.answer_location('40.551879047150194, 72.80027563597328')
    
@dp.message_handler(text='О нас')
async def your(message:types.Message):
    await message.answer('')
    
@dp.message_handler(text="Царский Двор")
async def samsa(message:types.Message):
    await message.answer("Кафе Царский Двор приветствует вас!", reply_markup=zarskyi_keyboard)
    
zarskyi_buttons = [
    types.KeyboardButton('Фотография'),
    types.KeyboardButton('Видео'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Назад')
]
zarskyi_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*zarskyi_buttons)

samsa_buttons = [
    types.KeyboardButton('Фотография'),
    types.KeyboardButton('Видео'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Назад')
]
samsa_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*samsa_buttons)

@dp.message_handler(text="Фотография")
async def photo(message:types.Message):
    await message.answer_photo('')
    await message.answer_photo('')
    await message.answer_photo('')
    await message.answer_photo('')
    
# @dp.message_handler(text="Видео")
# async def video(message:types.Message):
#     await message.answer_video('c:\\Users\\Welcome\\Pictures\\Saved Pictures\\ED4F4FDF1D726A2540C874F5E0B215AA_video_dashinit.mp4')
#     await message.answer_video('c:\\Users\\Welcome\\Pictures\\Saved Pictures\\0F44E0E452ED7B0CA540CD23C44D5EB1_video_dashinit.mp4')
    
@dp.message_handler(text='Адрес')
async def address(message:types.Message):
    await message.answer('')
    await message.answer_location('')
    
@dp.message_handler(text='О нас')
async def your(message:types.Message):
    await message.answer('')
    
@dp.message_handler(text="Ожак Кебаб")
async def samsa(message:types.Message):
    await message.answer("Кафе Ожак Кебаб приветствует вас!", reply_markup=kebab_keyboard)
    
kebab_buttons = [
    types.KeyboardButton('Фотография'),
    types.KeyboardButton('Видео'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Назад')
]
kebab_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*kebab_buttons)

@dp.message_handler(text="Фотография")
async def photo(message:types.Message):
    await message.answer_photo('')
    await message.answer_photo('')
    await message.answer_photo('')
    await message.answer_photo('')
    
# @dp.message_handler(text="Видео")
# async def video(message:types.Message):
#     await message.answer_video('c:\\Users\\Welcome\\Pictures\\Saved Pictures\\ED4F4FDF1D726A2540C874F5E0B215AA_video_dashinit.mp4')
#     await message.answer_video('c:\\Users\\Welcome\\Pictures\\Saved Pictures\\0F44E0E452ED7B0CA540CD23C44D5EB1_video_dashinit.mp4')
    
@dp.message_handler(text='Адрес')
async def address(message:types.Message):
    await message.answer('')
    await message.answer_location('')
    
@dp.message_handler(text='О нас')
async def your(message:types.Message):
    await message.answer('')
    
@dp.message_handler(text="Маленькая Япония")
async def samsa(message:types.Message):
    await message.answer("Кафе Маленькая Япония приветствует вас!", reply_markup=japan_keyboard)
    
japan_buttons = [
    types.KeyboardButton('Фотография'),
    types.KeyboardButton('Видео'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Назад')
]
japan_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*japan_buttons)

@dp.message_handler(text="Фотография")
async def photo(message:types.Message):
    await message.answer_photo('')
    await message.answer_photo('')
    await message.answer_photo('')
    await message.answer_photo('')
    
# @dp.message_handler(text="Видео")
# async def video(message:types.Message):
#     await message.answer_video('c:\\Users\\Welcome\\Pictures\\Saved Pictures\\ED4F4FDF1D726A2540C874F5E0B215AA_video_dashinit.mp4')
#     await message.answer_video('c:\\Users\\Welcome\\Pictures\\Saved Pictures\\0F44E0E452ED7B0CA540CD23C44D5EB1_video_dashinit.mp4')
    
@dp.message_handler(text='Адрес')
async def address(message:types.Message):
    await message.answer('')
    await message.answer_location('')
    
@dp.message_handler(text='О нас')
async def your(message:types.Message):
    await message.answer('')
    
@dp.message_handler(text="Суши тайм")
async def samsa(message:types.Message):
    await message.answer("Кафе Суши тайм приветствует вас!", reply_markup=sushi_keyboard)
    
sushi_buttons = [
    types.KeyboardButton('Фотография'),
    types.KeyboardButton('Видео'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Назад')
    
]
sushi_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*sushi_buttons)

@dp.message_handler(text="Фотография")
async def photo(message:types.Message):
    await message.answer_photo('https://lh3.googleusercontent.com/p/AF1QipOcTn7f1TMjU4NH9mMtUMQVrfVFTgeGtPB7OhIr=s1360-w1360-h1020')
    await message.answer_photo('https://lh3.googleusercontent.com/p/AF1QipNgTR8wV55SId_aZO-ueo-QVao7d_mFWFZW4VuH=s1360-w1360-h1020')
    await message.answer_photo('https://lh3.googleusercontent.com/p/AF1QipP7PYYQd2aE9rlTed0DFtjddNUgwaj-Dakak67o=s1360-w1360-h1020')
    await message.answer_photo('https://lh3.googleusercontent.com/p/AF1QipOVMc56TbvcSqYl6sXAEG2PblA6rmZShDaB_RUT=s1360-w1360-h1020')
    
@dp.message_handler(text="Видео")
async def video(message:types.Message):
    await message.answer_video('https://www.tiktok.com/@sushi_time.osh/video/7268291269057678599?is_from_webapp=1&sender_device=pc')
    await message.answer_video('https://www.tiktok.com/@sushi_time.osh/video/7314295439942077697?is_from_webapp=1&sender_device=pc')
    
@dp.message_handler(text='Адрес')
async def address(message:types.Message):
    await message.answer('452 Курманжан Датка, Ош')
    await message.answer_location('40.553723467945, 72.78163866140844')
    
@dp.message_handler(text='О нас')
async def your(message:types.Message):
    await message.answer('')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Чем могу помочь?", reply_markup=main_menu_keyboard)

@dp.message_handler(lambda message: message.text in ["Места где можно поесть", "Достопримечательности"])
async def handle_menu_buttons(message: types.Message):
    if message.text == "Места где можно поесть":
        await message.answer("Выберите кафе:", reply_markup=cafes_keyboard)
        for cafe_name in cafes_buttons:
            cafe = cafes_buttons[cafe_name]
            await message.answer_photo(cafe["photo"])
            await message.answer(f"<b>{cafe_name}</b>\n"
                                 f"<i>Адрес:</i> {cafe['address']}\n"
                                 f"{cafe['info']}\n", parse_mode="HTML")
    else:
        await message.answer(f"Вы выбрали: {message.text}")

review_chat_ids = {}

@dp.message_handler(lambda message: message.text == "Оставить отзыв")
async def leave_review(message: types.Message):
    review_chat_ids[message.chat.id] = None

    await message.answer("Введите ваше имя:")
    dp.register_message_handler(get_name)

async def get_name(message: types.Message):
    review_chat_ids[message.chat.id] = message.chat.id
    await message.answer("Введите ваш номер телефона:")
    dp.register_message_handler(get_phone)

async def get_phone(message: types.Message):
    await message.answer("Введите текст вашего отзыва:")
    dp.register_message_handler(send_review)

async def send_review(message: types.Message):
    chat_id = review_chat_ids.get(message.chat.id)
    if chat_id is not None:
        await bot.send_message(chat_id, f"Новый отзыв:\n"
                                         f"Имя: {message.from_user.full_name}\n"
                                         f"Номер телефона: {message.contact.phone_number}\n"
                                         f"Отзыв: {message.text}")
        await message.answer("Спасибо за ваш отзыв!")
    else:
        await message.answer("Что-то пошло не так. Пожалуйста, попробуйте еще раз.")

@dp.message_handler(lambda message: message.text == "Назад")
async def back(message: types.Message):
    await start(message)
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
