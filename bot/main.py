# основной файл бота без сложной логики 
#!!! не импортировать сторонние библиотеки только конкретные функции библиотеки from lib import * !!! 

import telebot
import config as cfg
from telebot import types
from telebot.apihelper import ApiTelegramException
from datetime import datetime

#самописные библиотеки импортируем польностью 
from registration import * 
from readexcel import *


#модули для дебага 
from time import sleep

#^^^^

#Желательно весь ввод проводить через перекодирование в utf-8 иначе при вводе незнакомых символов будет краш
#Или обработать исключение

                                                                                      
bot = telebot.TeleBot(cfg._TOKEN_)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    try:
        #Кнопки 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton('тарифы, акции и услуги')
        btn1 = types.KeyboardButton('Возможность до адреса')
        btn2 = types.KeyboardButton('Регистрация')
        markup.add(btn0, btn1,btn2)
        bot.send_message(message.chat.id,text = "Добрый день {0.first_name}, это - телеграм бот компании Ростелеком, в нем вы можете проверить возможность до адреса и узнать о тарифах".format(message.from_user),reply_markup=markup)
    except ApiTelegramException as e:
        print(e)
        

#Выбор функциональных групп 
@bot.message_handler(func=lambda message: True)
def reg(message):
    try:
        match (message.text):
            case ("тарифы, акции и услуги"):
                answer = serch_in_db(message.text,1)
                bot.send_message(message.chat.id, ("Вот все существующие тарифы:\n") + "\n".join(answer))
            case ("Возможность до адреса"):
                bot.send_message(message.chat.id, text = "Введите адрес в формате \"Уссурийск г.,Выгонная,16,121\" ")
                bot.register_next_step_handler(message, reanswer_serch)
            case ("Регистрация"):
                register_user(basename,message.from_user.first_name, str(message.chat.id))
                bot.send_message(message.chat.id, text = "Вы зарегистрированны")
    except ApiTelegramException as e:
        print(e)

def reanswer_serch(message):
    answer = serch_in_db(message.text,0)
    if answer == [] or answer == None or answer == 'Void':
        bot.send_message(message.chat.id, "По вашему адресу не обнаружены тарифы, проверьте правильность написания")
    else:bot.send_message(message.chat.id, ("Вам предоставлены следующие тарифы:\n") + " ".join(answer))

if __name__ == "__main__":
    basename = str(datetime.today())
    char = [':','.','+',' ']
    for i in range(len(char)):
        basename= basename.replace(char[i],'_')
    reg_init(basename)
    bot.polling(non_stop=True)

    
