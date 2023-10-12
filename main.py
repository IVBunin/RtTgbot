# основной файл бота без сложной логики 

#!!! не импортировать библиотеки from lib import * !!! 

import asyncio
import xlrd 
import random
import config as cfg
import prompts as prompt
from telebot import types
from telebot.apihelper import ApiTelegramException
from telebot.async_telebot import AsyncTeleBot

#Желательно весь ввод проводить через перекодирование в utf-8 иначе при вводе незнакомых символов будет краш
#Или обработать исключение

bot = AsyncTeleBot(cfg._TOKEN_)

async def writelog(txt):
    file = open('log.txt', 'a')
    file.write(txt +"\n")
    file.close
    print(txt)


# Обработка команды старт
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):


    try:
        #Кнопки 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton('Статус заявки')
        btn1 = types.KeyboardButton('Возможность до адреса')
        btn2 = types.KeyboardButton('Тестовый вывод')
        markup.add(btn0, btn1, btn2)
#Попробовать перенести текст из этой части с сохранением функции обращения
        bot.send_message(message.chat.id,text = "Добрый день {0.first_name}, это - телеграм бот компании Ростелеком, в нем вы можете проверить возможность до адреса и статус вашей заявки".format(message.from_user),reply_markup=markup)
    except ApiTelegramException as e:
        pass 
#Пока не функциональный код, надо решить{
@bot.message_handler(commands = ['address'])
async def adres_possibility(message):
    try: 
        bot.send_message(message.chat.id,prompt.text_enter_address)
    except ApiTelegramException as e:
        pass 

@bot.message_handler(commands=['application']) 
async def task_chek(message):
    try: 
        bot.send_message(message.chat.id,prompt.text_enter_application)
    except ApiTelegramException as e:
        pass 
   
#}  

#Обработка текстовых команд без /  с вводом с кнопок в начале 
@bot.message_handler(func=lambda message: True)
async def reg(message):
    id = message.chat.id
    txt =('('+ str(id)+')' + message.chat.username + ' : ' +str(message.text))
    await writelog(txt) 
    
    spreadsheet = xlrd.open_workbook('1.xls', formatting_info=True)
    sheet = spreadsheet.sheet_by_index(0)
    integ = random.randint(0,sheet.nrows-3)
    row = sheet.cell_value(rowx=integ, colx=1)
    print(row, integ)
    if message.text == 'Тестовый вывод':
        await bot.send_message(id, row)
    if message.text == 'Статус заявки':
        await bot.send_message(id,prompt.text_enter_application)
    if message.text == 'Возможность до адреса':
        await bot.send_message(id,prompt.text_enter_address)





asyncio.run(bot.polling())
