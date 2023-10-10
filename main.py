import telebot
import config as cfg
from telebot.apihelper import ApiTelegramException

#@bot.message_handler(content_types = ['comand name']) 

bot = telebot.TeleBot(cfg._TOKEN_)



bot.infinity_polling(none_stop=True, timeout=10)