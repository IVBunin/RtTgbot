import telebot
import config as cfg
from telebot.apihelper import ApiTelegramException

#@bot.message_handler(content_types = ['comand name']) 

bot = telebot.TeleBot(cfg._TOKEN_)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    try:
        bot.send_message(message.chat.id,text = "Привет {0.first_name}. я бот \n/butons - выводит кнопки \n Так же он принимает картинки 😉😉😉".format(message.from_user))
        
    except ApiTelegramException as e:
        pass 
bot.infinity_polling(none_stop=True, timeout=10)