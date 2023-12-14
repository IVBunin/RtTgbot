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
        btn1 = types.KeyboardButton('Информационные услуги')
        btn2 = types.KeyboardButton('Информационные услуги 2')
        btn3 = types.KeyboardButton('?')
        btn4 = types.KeyboardButton('<=')
        btn5 = types.KeyboardButton('✉️')
        markup.add(btn0, btn1, btn2, btn3, btn4, btn5)
        await bot.send_message(message.chat.id,text = "Добрый день {0.first_name}, это - телеграм бот компании Ростелеком, в нем вы можете проверить возможность до адреса и статус вашей заявки".format(message.from_user),reply_markup=markup)
    except ApiTelegramException as e:
        raise(Exception)

#Выбор функциональных групп 
@bot.message_handler(func=lambda message: True)
async def reg(message):
    try:
        if message.text == "тарифы, акции и услуги":
            await bot.send_message(message.chat.id, text = "a1")

        if message.text == "Информационные услуги":
            await bot.send_message(message.chat.id, text = " a2")

        if message.text == "Информационные услуги 2":
            await bot.send_message(message.chat.id, text = " 3")

        if message.text == "<=":
            await bot.send_message(message.chat.id, text = "a4 ")

        if message.text == "?":
            await bot.send_message(message.chat.id, text = " a5")

        if message.text == "✉️":
            await bot.send_message(message.chat.id, text = " a6")

    except ApiTelegramException as e:
        raise(Exception)
        
if __name__ == "__main__":
    asyncio.run(bot.polling())
