# основной файл бота без сложной логики 
#!!! не импортировать библиотеки from lib import * !!! 
import asyncio
import config as cfg
from telebot import types
from telebot.apihelper import ApiTelegramException
from telebot.async_telebot import AsyncTeleBot
from main_logic import * #Тут можно 
#Желательно весь ввод проводить через перекодирование в utf-8 иначе при вводе незнакомых символов будет краш
#Или обработать исключение


bot = AsyncTeleBot(cfg._TOKEN_)


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    try:
        #Кнопки 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton('тарифы, акции и услуги')
        btn1 = types.KeyboardButton('Возможность до адреса')
        markup.add(btn0, btn1)
        await bot.send_message(message.chat.id,text = "Добрый день {0.first_name}, это - телеграм бот компании Ростелеком, в нем вы можете проверить возможность до адреса и узнать о тарифах".format(message.from_user),reply_markup=markup)
    except ApiTelegramException as e:
        print(e)

#Выбор функциональных групп 
@bot.message_handler(func=lambda message: True)
async def reg(message):
    try:

        if message.text == "тарифы, акции и услуги":
            await bot.send_message(message.chat.id, text = "Введите тариф")

        if message.text == "Возможность до адреса":
            await bot.send_message(message.chat.id, text = "Введите адрес")
            
    except ApiTelegramException as e:
        print(e)


@bot.message_handler(func=lambda message: True)
async def serch_in_db_adress(message):
    try:
# 0 - параметр для вывода адреса
        await bot.send_message(message.chat.id, text = f"Тарифы для вашего адреса = {serch_in_db(message.text,0)}")
    except ApiTelegramException as e:
        print(e)

@bot.message_handler(func=lambda message: True)
async def serch_in_db_adress(message):
    try:
# 1 - параметр для вывода тарифов
        await bot.send_message(message.chat.id, text = f"Тарифы = {serch_in_db( "void", 1)}")
    except ApiTelegramException as e:
        print(e)


if __name__ == "__main__":
    asyncio.run(bot.polling())
