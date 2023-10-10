import telebot
import config as cfg
import prompts as prompt
from telebot.apihelper import ApiTelegramException

#@bot.message_handler(content_types = ['comand name']) 

bot = telebot.TeleBot(cfg._TOKEN_)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    try:
         bot.send_message(message.chat.id,text = prompt.text_0)
        
    except ApiTelegramException as e:
        pass 

@bot.message_handler(commands=['comand1']) 
def adres_possibility(message):
    try: 
        bot.send_message(message.chat.id,prompt.text_1)
    except ApiTelegramException as e:
        pass 

@bot.message_handler(commands=['comand2']) 
def task_chek(message):
    try: 
        bot.send_message(message.chat.id,prompt.text_2)
    except ApiTelegramException as e:
        pass 


@bot.message_handler(content_types = ['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)

bot.infinity_polling(none_stop=True, timeout=10)