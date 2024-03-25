# from aiogram import Bot, Dispatcher, types, executor
# from config import tokens
# import logging

# bot = Bot(token=tokens)
# dp = Dispatcher(bot)
# logging.basicConfig(level=logging.INFO)

# courses_buttons = [
#     types.KeyboardButton('Модели автомобилей'),
#     types.KeyboardButton('Цены'),
#     types.KeyboardButton('Характеристики'), 
#     types.KeyboardButton('Специальные предложения'),
#     types.KeyboardButton('Назад')
# ]
# courses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*courses_buttons)

# @dp.message_handler(commands='start')
# async def start(message:types.Message):
#     await message.answer('Здраствуйте, чем могу помочь?', reply_markup=courses_keyboard)
    
# @dp.message_handler(commands='help')
# async def help(message:types.Message):
#     await message.answer('Напишите свою проблему.', reply_markup=courses_keyboard)

# coues_buttons = [
#     types.KeyboardButton('BMW IX M6'),
#     types.KeyboardButton('BMW M5'),
#     types.KeyboardButton('BMW M3'), 
#     types.KeyboardButton('BMW M4'),
#     types.KeyboardButton('Назад')
# ]
# couses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*coues_buttons) 
    
# @dp.message_handler(text="Модели автомобилей")
# async def all_courses(message:types.Message):
#     await message.answer("Вот все наши автомобили:", reply_markup=couses_keyboard)

# @dp.message_handler(text="Назад")
# async def back(message:types.Message):
#     await start(message)

# @dp.message_handler(text="BMW IX M6")
# async def bmw(message:types.Message):
#     await message.answer_photo('https://www.bmw.kg/content/dam/bmw/common/all-models/m-series/iX-60/2021/onepager/bmw-ix-m60-onepager-mc-performance-design-highlights-hero-desktop.jpg/jcr:content/renditions/cq5dam.resized.img.1680.large.time1636554778108.jpg')
#     await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/bmw-ix-m60/2021/bmw-ix-m60-highlights/jcr:content/par/multicontent_1948771425/tabs/multicontenttab/items/smallteaser_92fb/image.transform/smallteaser/image.1659701303655.jpg')
#     await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/bmw-ix-m60/2021/bmw-ix-m60-highlights/jcr:content/par/multicontent_1948771425/tabs/multicontenttab/items/smallteaser_807d/image.transform/smallteaser/image.1659701303694.jpg')
#     await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/bmw-ix-m60/2021/bmw-ix-m60-highlights/jcr:content/par/multicontent_1948771425/tabs/multicontenttab/items/smallteaser_e652/image.transform/smallteaser/image.1659701303759.jpg')
#     await message.answer_photo('https://www.bmw.kg/content/dam/bmw/common/all-models/m-series/iX-60/2021/onepager/bmw-ix-m60-onepager-ms-shytech-02.jpg/jcr:content/renditions/cq5dam.resized.img.585.low.time1636554826615.jpg')
#     await message.answer_photo('https://www.bmw.kg/content/dam/bmw/common/all-models/m-series/iX-60/2021/onepager/bmw-ix-m60-onepager-gallery-impressions-thumbnail-09.jpg/jcr:content/renditions/cq5dam.resized.img.890.medium.time1707923935083.jpg')
#     await message.answer_photo('https://www.bmw.kg/content/dam/bmw/common/all-models/m-series/iX-60/2021/onepager/bmw-ix-m60-onepager-gallery-impressions-thumbnail-02.jpg/jcr:content/renditions/cq5dam.resized.img.890.medium.time1634643882707.jpg')
#     await message.answer_photo('https://www.bmw.kg/content/dam/bmw/common/all-models/m-series/iX-60/2021/onepager/bmw-ix-m60-onepager-gallery-impressions-thumbnail-05.jpg/jcr:content/renditions/cq5dam.resized.img.890.medium.time1707923934759.jpg')
#     await message.answer_photo('https://www.bmw.kg/content/dam/bmw/common/all-models/m-series/iX-60/2021/onepager/bmw-ix-m60-onepager-gallery-impressions-thumbnail-06.jpg/jcr:content/renditions/cq5dam.resized.img.890.medium.time1640271472575.jpg')
    
# @dp.message_handler(text="BMW M5")
# async def mers(message:types.Message):
#     await message.answer('https://www.youtube.com/watch?v=qHQaLs1nypg')

# @dp.message_handler(text="BMW M3")
# async def camry(message:types.Message):
#     await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/m3-sedan/2023/bmw-3-series-sedan-m-automobiles-overview/jcr:content/par/multicontent/tabs/multicontenttab_copy/items/smallteaser/image.transform/smallteaser/image.1685595080472.jpg')
#     await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/m3-sedan/2023/bmw-3-series-sedan-m-automobiles-overview/jcr:content/par/multicontent/tabs/multicontenttab_copy/items/smallteaser_copy/image.transform/smallteaser/image.1685595080513.jpg')
#     await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/m3-sedan/2023/bmw-3-series-sedan-m-automobiles-overview/jcr:content/par/multicontent/tabs/multicontenttab_copy/items/smallteaser_copy_cop/image.transform/smallteaser/image.1685595080591.jpg')
#     await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/m3-sedan/2023/bmw-3-series-sedan-m-automobiles-overview/jcr:content/par/multicontent/tabs/multicontenttab_copy_1506470107/items/smallteaser/image.transform/smallteaser/image.1685595080680.jpg')
#     await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/m3-sedan/2023/bmw-3-series-sedan-m-automobiles-overview/jcr:content/par/multicontent/tabs/multicontenttab_copy_1506470107/items/smallteaser_copy/image.transform/smallteaser/image.1685595080725.jpg')
#     await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/m3-sedan/2023/bmw-3-series-sedan-m-automobiles-overview/jcr:content/par/multicontent/tabs/multicontenttab_copy_1506470107/items/smallteaser_copy_cop/image.transform/smallteaser/image.1685595080772.jpg')

# @dp.message_handler(text="BMW M4")
# async def lexus(message:types.Message):
#     await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/m4-coupe/2022/bmw-4-series-coupe-m-automobiles-highlights/jcr:content/par/multicontent/tabs/multicontenttab_copy/items/smallteaser/image.transform/smallteaser/image.1672115152308.jpg')
#     await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/m4-coupe/2022/bmw-4-series-coupe-m-automobiles-highlights/jcr:content/par/multicontent/tabs/multicontenttab_copy/items/smallteaser_copy/image.transform/smallteaser/image.1672115152361.jpg')
#     await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/m4-coupe/2022/bmw-4-series-coupe-m-automobiles-highlights/jcr:content/par/multicontent/tabs/multicontenttab_copy/items/smallteaser_copy_cop/image.transform/smallteaser/image.1672115152431.jpg')
#     await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/m4-coupe/2022/bmw-4-series-coupe-m-automobiles-highlights/jcr:content/par/multicontent/tabs/multicontenttab_1535450737/items/smallteaser_copy_cop/image.transform/smallteaser/image.1672115152943.jpg')
#     await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/m4-coupe/2022/bmw-4-series-coupe-m-automobiles-highlights/jcr:content/par/multicontent/tabs/multicontenttab_1535450737/items/smallteaser/image.transform/smallteaser/image.1672115152894.jpg')
#     await message.answer_photo('https://www.bmw.kg/content/bmw/marketB4R1/bmw_kg/ru_KG/all-models/m-series/m4-coupe/2022/bmw-4-series-coupe-m-automobiles-highlights/jcr:content/par/multicontent/tabs/multicontenttab_249504282/items/smallteaser/image.transform/smallteaser/image.1672115152610.jpg')

# couses_buttons = [
#     types.KeyboardButton('цена - BMW IX M6'),
#     types.KeyboardButton('цена - BMW M5'),
#     types.KeyboardButton('цена - BMW M3'), 
#     types.KeyboardButton('цена - BMW M4'),
#     types.KeyboardButton('Назад')
# ]
# couсes_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*couses_buttons) 

# @dp.message_handler(text='Цены')
# async def zena(message:types.Message):
#     await message.answer("Вот цены автомобилей", reply_markup=couсes_keyboard)


# @dp.message_handler(text="цена - BMW IX M6")
# async def bmw7(message:types.Message):
#     await message.answer("12 000 000 c")

# @dp.message_handler(text="цена - BMW M5")
# async def bmwm5(message:types.Message):
#     await message.answer("5 580 000 c")

# @dp.message_handler(text="цена - BMW M3")
# async def bmwm3(message:types.Message):
#     await message.answer("8 000 000 c")

# @dp.message_handler(text="цена - BMW M4")
# async def bmwm4(message:types.Message):
#     await message.answer("6 500 000 c")

# @dp.message_handler(text="Назад")
# async def back(message:types.Message):
#     await start(message)
    
# cotues_buttons = [
#     types.KeyboardButton('характеристика - BMW IX M6'),
#     types.KeyboardButton('характеристика - BMW M5'),
#     types.KeyboardButton('характеристика - BMW M3'), 
#     types.KeyboardButton('характеристика - BMW M4'),
#     types.KeyboardButton('Назад')
# ]
# courtses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*cotues_buttons) 

# @dp.message_handler(text="Характеристики")
# async def all_courses(message:types.Message):
#     await message.answer("Вот характеристики автомобилей:", reply_markup=courtses_keyboard)
    
# @dp.message_handler(text="Модели автомобилей")
# async def all_courses(message:types.Message):
#     await message.answer("Вот все наши автомобили:", reply_markup=courtses_keyboard)

# @dp.message_handler(text="Назад")
# async def back(message:types.Message):
#     await start(message)

# @dp.message_handler(text="характеристика - BMW IX M6")
# async def bmw(message:types.Message):
#     await message.answer('''Мощность двигателя в кВт (л.с.):      455 (619)**\n

# \nРазгон 0–100 км/ч в секундах:      3,8*

# \nЗапас хода на электротяге (WLTP), км:      575*

# \nКрутящий момент в Нм при 1/мин:      1 100***

# \nЭнергопотребление в кВтч/100 км (WLTP):      21,6*    

# ''')
    
# @dp.message_handler(text="характеристика - BMW M5")
# async def mers(message:types.Message):
#     await message.answer('''Мощность, л.с.:      460 (625)\n

# Разгон 0–100 км/ч, с:      3.9\n

# Расход топлива в смешанном цикле WLTP, л/100 км:      13.1–12.8\n

# Выбросы CO2 в смешанном цикле WLTP, г/км:      296–288\n

# ''')

# @dp.message_handler(text="характеристика - BMW M3")
# async def camry(message:types.Message):
#     await message.answer('''Мощность, л.с.:      405 (551)\n

# Крутящий момент, Нм:      650\n

# Разгон 0-100 км/ч, с:       3,4\n

# Расход топлива в смешанном цикле WLTP, л/100 км:      10,4–10,1\n

# ''')

# @dp.message_handler(text="характеристика - BMW M4")
# async def lexus(message:types.Message):
#     await message.answer('''Мощность, кВт (л.с.) при об/мин:      405 (551)/6,250\n

# \nМакс. крутящий момент, Нм при об/мин:      650/2,750-5,950

# \nРазгон 0–100 км/ч в секундах:      3.7

# \nРасход топлива в л/100 км (смешанный цикл):      10.1

# ''')

# couses_buttons = [
#     types.KeyboardButton('цена - BMW IX M6'),
#     types.KeyboardButton('цена - BMW M5'),
#     types.KeyboardButton('цена - BMW M3'), 
#     types.KeyboardButton('цена - BMW M4'),
#     types.KeyboardButton('Назад')
# ]
# couсes_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*couses_buttons) 

# @dp.message_handler(text='Цены')
# async def zena(message:types.Message):
#     await message.answer("Вот цены автомобилей", reply_markup=couсes_keyboard)


# @dp.message_handler(text="цена - BMW IX M6")
# async def bmw7(message:types.Message):
#     await message.answer("12 000 000 c")

# @dp.message_handler(text="цена - BMW M5")
# async def bmwm5(message:types.Message):
#     await message.answer("5 580 000 c")

# @dp.message_handler(text="цена - BMW M3")
# async def bmwm3(message:types.Message):
#     await message.answer("8 000 000 c")

# @dp.message_handler(text="цена - BMW M4")
# async def bmwm4(message:types.Message):
#     await message.answer("6 500 000 c")

# @dp.message_handler(text="Назад")
# async def back(message:types.Message):
#     await start(message)
    


# @dp.message_handler(text='Специальные предложения')
# async def zena(message:types.Message):
#     await message.answer("""Если вы у нас будите покупать машины, то у нас даеться гарантия на 10 лет.\n
# При покупке машин тонировка + чехол идет в подарок!""")

# @dp.message_handler()
# async def about_us(message:types.Message):
#     await message.reply("я вас не понял")

# executor.start_polling(dp)