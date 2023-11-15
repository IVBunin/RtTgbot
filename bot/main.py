# основной файл бота без сложной логики 
#!!! не импортировать библиотеки from lib import * !!! 
import asyncio
import config as cfg
from telebot import types
from telebot.apihelper import ApiTelegramException
from telebot.async_telebot import AsyncTeleBot

#Желательно весь ввод проводить через перекодирование в utf-8 иначе при вводе незнакомых символов будет краш
#Или обработать исключение


bot = AsyncTeleBot(cfg._TOKEN_)


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    try:
        #Кнопки 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton('Статус заявки')
        btn1 = types.KeyboardButton('Возможность до адреса')
        btn2 = types.KeyboardButton('Тестовый вывод')
        markup.add(btn0, btn1, btn2)
        await bot.send_message(message.chat.id,text = "Добрый день {0.first_name}, это - телеграм бот компании Ростелеком, в нем вы можете проверить возможность до адреса и статус вашей заявки".format(message.from_user),reply_markup=markup)
    except ApiTelegramException as e:
        raise(Exception)

#Выбор функциональных групп 
@bot.message_handler(func=lambda message: True)
async def reg(message):
    try:
        if message.text == "Информационные услуги":
            bot.send_message(message.chat.id, text = " ", reply_markup=markup)
            bot.register_next_step_handler(message, function_choise)

        if message.text == "Услуги продаж":
            bot.send_message(message.chat.id, text = " ", reply_markup=markup)
            bot.register_next_step_handler(message, start)

    except ApiTelegramException as e:
        raise(Exception)


@bot.message_handler(func=lambda message: True)
async def function_choise(message):
    try:
        if message.text == "тарифы, акции и услуги":
            bot.send_message(message.chat.id, text = " ", reply_markup=markup)
            bot.register_next_step_handler(message, function_choise)

        if message.text == "Информационные услуги":
            bot.send_message(message.chat.id, text = " ", reply_markup=markup)
            bot.register_next_step_handler(message, start)

        if message.text == "Информационные услуги":
            bot.send_message(message.chat.id, text = " ",reply_markup=markup)
    
    except ApiTelegramException as e:
        raise(Exception)





asyncio.run(bot.polling())
