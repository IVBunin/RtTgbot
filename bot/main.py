# основной файл бота без сложной логики 
#!!! не импортировать сторонние библиотеки только конкретные функции библиотеки from lib import * !!! 

import telebot
import config as cfg
from telebot import types
from telebot.apihelper import ApiTelegramException
from os import listdir
import os


#самописные библиотеки импортируем польностью 
from registration import * 
from readexcel import *

#^^^^

#Желательно весь ввод проводить через перекодирование в utf-8 иначе при вводе незнакомых символов будет краш
#Или обработать исключение

                                                                                      
bot = telebot.TeleBot(cfg._TOKEN_)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message): # Старт бота
    try:
        #Кнопки 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton('Регистрация')
        markup.add(btn0)
        bot.send_message(message.chat.id,text = "Добрый день {0.first_name}, это - телеграм бот помошник в продажах. Пожалйста, пройдите регистрацию".format(message.from_user),reply_markup=markup)
    except ApiTelegramException as e:
        print(e)
 
@bot.message_handler(func=lambda message: True) 
def reg(message): #Функциональный блок
    try:
        match (message.text):
            case ("тарифы, акции и услуги"):
                answer = all_options()
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
            case("Мои заявки"):
                bot.send_message(message.chat.id, "Вот все ваши заявки:\n"+"".join(ask_answer(get_from_reg(basename, "chat_id", message.chat.id))))
            case("Обращение к оракулу"):
                bot.send_message(message.chat.id, "Что бы вы хотели узнать у всезнающего оракула?")
                bot.register_next_step_handler(message, chatwgpt)
            case("Статистика"):
                bot.send_message(message.chat.id, "Для получения информации о СЦ, введите имя СЦ в формате \"СЦ Северо-Восточный\"\nО вас: \n" + str(done_requests(get_from_reg(basename,"chat_id",message.chat.id))))
                bot.register_next_step_handler(message, infograph)
            case("Обратная связь"):
                bot.send_message(message.chat.id, "Отправьте следующим сообщением текст для обратной связи. \n Вы можете отменить это действие отправив\"Отмена\"")
                bot.register_next_step_handler(message,backansw)
    except ApiTelegramException as e:
        print(e)

def registration_c(message): #Блок после регистрации
    try:
        names = get_keys(basename)
        if message.text in names:
            register_user(basename,message.text,message.chat.id)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("тарифы, акции и услуги")
            btn2= types.KeyboardButton("Возможность до адреса")
            btn3= types.KeyboardButton("Мои заявки")
            btn4= types.KeyboardButton("Обращение к оракулу")
            btn5 = types.KeyboardButton("Статистика")
            btn6 = types.KeyboardButton("Обратная связь")
            markup.add(btn1,btn2,btn3,btn4,btn5,btn6)
            bot.send_message(message.chat.id, "Вы зарегистрированны",reply_markup=markup)
        else: 
            bot.send_message(message.chat.id, "Вас нет в списке")
    except ApiTelegramException as e:
        print(e)
        bot.send_message("Что-то сломалось")
        return e

def backansw(message):
    try:
        if message.text != 'Отмена':
            base = open(cfg._LOCAL_BASE_PATH_ + "Обратная_связь.txt", "a")
            base.write(get_from_reg(basename, type_="chat_id", request= message.chat.id) +" : " + message.text)
            bot.send_message(message.chat.id, "Отработал")
            base.close()
        else: bot.send_message(message.chat.id, "Рассылка отменена 👍")
    except ApiTelegramException as e:
        return e

def infograph(message):
    try:
        answer = alldone_requests(message.text)
        if answer == [] or answer == None or answer == 'Void':
            bot.send_message(message.chat.id, "Ваш СЦ не обнаружен, проверьте правильность написания")
        else:bot.send_message(message.chat.id, "Вот количество выполненных задач по отделу:\n" + " ".join(answer))
    except ApiTelegramException as e:
        print(e)
        bot.send_message("Что-то сломалось")
        return e

def chatwgpt(message): #Т.к. токен не работает, было решено добавить "игру"
    try:
        if message.text == None: bot.send_message(message.chat.id, "Оракул не принимает визуальные образы")
        else:
            bot.send_message(message.chat.id,"Вот все говорят: " + message.text + "\nА ты купи слона.")
        #bot.send_message(askGPT(message.text)) 
    except ApiTelegramException as e:
        print(e)
        bot.send_message("Что-то сломалось")
        return e

def reanswer_serch(message): #Возможность до адреса
    try:
        answer = serch_in_db(message.text)
        if answer == [] or answer == None or answer == 'Void':
            bot.send_message(message.chat.id, "По вашему адресу не обнаружены тарифы, проверьте правильность написания")
        else:bot.send_message(message.chat.id, "Вам предоставлены следующие тарифы:\n" + " ".join(answer))
    except ApiTelegramException as e:
        print(e)
        bot.send_message("Что-то сломалось")
        return e

def send_messages(message): #Рассылка
    try:
        if message.text != 'Отмена':
            base = open(cfg._LOCAL_BASE_PATH_ + basename, "r")
            data = json.load(base)
            for key,value in data["items"].items():
                if value != str(): 
                    bot.forward_message(value, message.chat.id, message.message_id)
            bot.send_message(message.chat.id, "Отработал")
        else: bot.send_message(message.chat.id, "Рассылка отменена 👍")
    except ApiTelegramException as e:
        print(e)
        bot.send_message("Что-то сломалось")
        return e


if __name__ == "__main__": # Создание базы
    if not listdir(cfg._LOCAL_BASE_PATH_):
        basename = str("base")
        reg_init(basename)
        
        for file_name in listdir(cfg._LOCAL_BASE_PATH_):
                basename = str(file_name)
                basename = basename 
        reg_list =  find_all_people()
        for i in range(len(reg_list)):
            register_user(basename, reg_list[i] , "")
    for file_name in listdir(cfg._LOCAL_BASE_PATH_):
            basename = str(file_name)
   # create_app()
    bot.polling(non_stop=True)
    
    
