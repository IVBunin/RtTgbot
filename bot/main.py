# основной файл бота без сложной логики 
#!!! не импортировать сторонние библиотеки только конкретные функции библиотеки from lib import * !!! 

import telebot
import config as cfg
from telebot import types
from telebot.apihelper import ApiTelegramException
from datetime import datetime
from os import listdir

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
        btn0 = types.KeyboardButton('Регистрация')
        markup.add(btn0)
        bot.send_message(message.chat.id,text = "Добрый день {0.first_name}, это - телеграм бот помошник в продажах. Пожалйста, пройдите регистрацию".format(message.from_user),reply_markup=markup)
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
                bot.send_message(message.chat.id, text = "Введите ваше фио по образцу 'Фамилия Имя Отчество' ")
                bot.register_next_step_handler(message, registration_c)
            case("Рассылка"):
                bot.send_message(message.chat.id, 'Отправьте сообщение для рассылки.\n Вы можете отменить рассылку отправив \"Отмена\"')
                bot.register_next_step_handler(message,send_messages)
    except ApiTelegramException as e:
        print(e)


def reanswer_serch(message):
    try:
        answer = serch_in_db(message.text,0)
        if answer == [] or answer == None or answer == 'Void':
            bot.send_message(message.chat.id, "По вашему адресу не обнаружены тарифы, проверьте правильность написания")
        else:bot.send_message(message.chat.id, ("Вам предоставлены следующие тарифы:\n") + " ".join(answer))
    except ApiTelegramException as e:
        print(e)


def registration_c(message):
    try:
        names = get_keys(basename)
        if message.text in names:
            register_user(basename,message.text,message.chat.id)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("тарифы, акции и услуги")
            btn2= types.KeyboardButton("Возможность до адреса")
            markup.add(btn1,btn2)
            bot.send_message(message.chat.id, "Вы зарегистрированны",reply_markup=markup)
        else: 
            bot.send_message(message.chat.id, "Вас нет в списке")
    except ApiTelegramException as e:
        print(e)
      
def send_messages(message):
    try:
        if (message.text).lower == 'отмена':
            base = open(f"bot/data/base/{basename}", "r")
            data = json.load(base)
            for key,value in data["items"].items():
                if value != (str() or None): 
                    bot.forward_message(value, message.chat.id, message.message_id)
            bot.send_message(message.chat.id, "Отработал")
        else: bot.send_message(message.chat.id, "Рассылка отменена 👍")
    except ApiTelegramException as e:
        print(e)


if __name__ == "__main__":
    if not listdir("data/base/"):
        basename = str(datetime.today())
        char = [':','.','+',' ']
        for i in range(len(char)):
            basename= basename.replace(char[i],'_')
        reg_init(basename)
        
        for file_name in listdir("data/base/"):
                basename = str(file_name)
                basename = basename 
        reg_list =  serch_in_db(" ", 2)
        for i in range(len(reg_list)):
            register_user(basename, reg_list[i] , "")
    for file_name in listdir("data/base/"):
            basename = str(file_name)

    bot.polling(non_stop=True)

    
