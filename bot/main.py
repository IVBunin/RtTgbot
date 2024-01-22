# основной файл бота без сложной логики 
#!!! не импортировать сторонние библиотеки только конкретные функции библиотеки from lib import * !!! 

import asyncio
import config as cfg
from telebot import types
from telebot.apihelper import ApiTelegramException
from telebot.async_telebot import AsyncTeleBot
from datetime import datetime

#самописные библиотеки импортируем польностью 
from registration import * 
from readexcel import *


#модули для дебага 
from time import sleep

#^^^^

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
        btn2 = types.KeyboardButton('Регистрация')
        markup.add(btn0, btn1,btn2)
        await bot.send_message(message.chat.id,text = "Добрый день {0.first_name}, это - телеграм бот компании Ростелеком, в нем вы можете проверить возможность до адреса и узнать о тарифах".format(message.from_user),reply_markup=markup)
    except ApiTelegramException as e:
        print(e)
        

#Выбор функциональных групп 
@bot.message_handler(func=lambda message: True)
async def reg(message):
    try:
        await bot.send_message(message.chat.id, text = " ".join(serch_in_db(message.text, 0)))
        match (message.text):
            case ("тарифы, акции и услуги"):
                await bot.send_message(message.chat.id, text = "Введите тариф")
            case ("Возможность до адреса"):
                await bot.send_message(message.chat.id, text = "Введите адрес в формате \"Уссурийск г.,Выгонная,16,121\" ")
            case ("Регистрация"):
                register_user(basename,message.from_user.first_name, str(message.chat.id))
                await bot.send_message(message.chat.id, text = "Вы зарегистрированны")
    except ApiTelegramException as e:
        print(e)


if __name__ == "__main__":
    basename = str(datetime.today())
    char = [':','.','+',' ']
    for i in range(len(char)):
        basename= basename.replace(char[i],'_')
    reg_init(basename)
    asyncio.run(bot.polling())

    
