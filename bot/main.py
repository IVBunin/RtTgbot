# основной файл бота без сложной логики 
#!!! не импортировать библиотеки from lib import * !!! 
import asyncio
import config as cfg
from telebot import types
from telebot.apihelper import ApiTelegramException
from telebot.async_telebot import AsyncTeleBot

#Желательно весь ввод проводить через перекодирование в utf-8 иначе при вводе незнакомых символов будет краш
#Или обработать исключение

#файл prompt.py переехал в данные полученые с апи которые надо запоминать. Вывод в отдельный файл


bot = AsyncTeleBot(cfg._TOKEN_)

async def writelog(txt):
    file = open('log.txt', 'a', encoding='UTF-8')
    file.write(txt +"\n")
    file.close
    print(txt)

#Работа с таблицей для разовой записи

spreadsheet = xlrd.open_workbook('1.xls', formatting_info=True)
sheet = spreadsheet.sheet_by_index(0)
dict_answ = {}
for rownum in range(sheet.nrows-1):
    dict_answ[sheet.cell_value(rownum,colx=1)]= sheet.cell_value(rownum,colx=2)
print('Таблица подгружена, бот работает')



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
        await bot.send_message(message.chat.id,text = "Добрый день {0.first_name}, это - телеграм бот компании Ростелеком, в нем вы можете проверить возможность до адреса и статус вашей заявки".format(message.from_user),reply_markup=markup)
    except ApiTelegramException as e:
        pass 

#Обработка текстовых команд без /  с вводом с кнопок в начале 

@bot.message_handler(func=lambda message: True)
async def reg(message):
    try:
        id = message.chat.id
        txt =('('+ str(id)+')' + str(message.chat.username) + ' : ' +str(message.text))
        integ = random.randint(0,sheet.nrows)
        row = sheet.cell_value(rowx=integ, colx=1)
        await writelog(txt) 
        if message.text == 'Тестовый вывод':
            await bot.send_message(id, row)
        if message.text == 'Статус заявки':
            await bot.send_message(id,prompt.text_enter_application)
        if message.text == 'Возможность до адреса':
            await bot.send_message(id,prompt.text_enter_address)
        for k, v in dict_answ.items():
            if message.text == k:
                await bot.send_message(id, "Ваша заявка - " + v)
                await writelog("BOT: Ваша заявка - " + v)
        if message.text == 'sticker':
            await bot.send_sticker(id, 'CAACAgIAAxkBAAJGmGUoBkAbKeKzEaCZmZcxbGYbK280AAJ4IQACnByASozXcJvrjGo_MAQ')
    #Обработка ошибок        
        if (message.text not in rows_list) & (message.text != 'Тестовый вывод') & (message.text != 'Статус заявки') & (message.text != 'Возможность до адреса'):
            await bot.send_message(id, 'Проверьте корректность')
    except ApiTelegramException as e:
        pass





asyncio.run(bot.polling())
