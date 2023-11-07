import telebot 
from telebot import types
from telebot.apihelper import ApiTelegramException
from telebot.async_telebot import AsyncTeleBot
from random import randint

import config as cfg
import prompts as prompt




bot = telebot.TeleBot(cfg._TOKEN_)

def rand_speed():
    speed_list = (10,100,300)
    return speed_list[randint(0,2)]
    

@bot.message_handler(commands=['help', 'start'])
def enter(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Возможность до адреса')
        markup.add(btn1)
        bot.send_message(message.chat.id,text = "Добрый день {0.first_name}, это - телеграм бот компании Ростелеком, в нем вы можете проверить возможность до адреса и статус вашей заявки".format(message.from_user),reply_markup=markup)
    except:
        pass

@bot.message_handler(func=lambda message: True)
def comand_handler(message):
    try:
        id = message.chat.id
        if message.text == 'Возможность до адреса':
            bot.send_message(id,prompt.text_enter_address)
            bot.register_next_step_handler(message, adres_output)
           
    except:
        pass

def adres_output(message):
    text = str(message.text) 
    if "Ул" or "ул" or "УЛ" in text:
        bot.send_message(message.chat.id, text = f"По вашему адресу максимальная скорость = {rand_speed()}")
    else:
        bot.send_message(message.chat.id, text = "Неверный формат адреса")
        
    

bot.infinity_polling(none_stop=True, timeout=10)