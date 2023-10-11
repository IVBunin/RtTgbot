import telebot
import config as cfg
import prompts as prompt
from telebot import types
from telebot.apihelper import ApiTelegramException

#@bot.message_handler(content_types = ['comand name']) 

bot = telebot.TeleBot(cfg._TOKEN_)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton('Статус заявки')
        btn1 = types.KeyboardButton('Возможность до адреса')
        markup.add(btn0,btn1)
        bot.send_message(message.chat.id,text = "Добрый день {0.first_name}, это - телеграм бот компании Ростелеком, в нем вы можете проверить возможность до адреса и статус вашей заявки".format(message.from_user),reply_markup=markup)
    except ApiTelegramException as e:
        pass 

@bot.message_handler(commands = ['address'])
def adres_possibility(message):
    try: 
        bot.send_message(message.chat.id,prompt.text_enter_address)
    except ApiTelegramException as e:
        pass 

@bot.message_handler(commands=['application']) 
def task_chek(message):
    try: 
        bot.send_message(message.chat.id,prompt.text_enter_application)
    except ApiTelegramException as e:
        pass 
    
@bot.message_handler(func=lambda message: True)
def reg(message):
    if message.text == 'Статус заявки':
        bot.send_message(message.chat.id,prompt.text_enter_application)
    if message.text == 'Возможность до адреса':
        bot.send_message(message.chat.id,prompt.text_enter_address)



bot.infinity_polling(none_stop=True, timeout=10)
