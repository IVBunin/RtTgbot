import telebot
import time
import aiogram



@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.chat.id, 'Введите то то')
    bot.register_next_step_handler(msg, start_2)


def start_2(message):
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id - 1, text='вы ввели ' + message.text)
    
@tb.message_handler(func=lambda m: True)
def echo_all(message):
    try:
           time.sleep(20) # to make delay 
           ret_msg=tb.reply_to(message, "response message") 
           print(ret_msg)
           assert ret_msg.content_type == 'text'
    except TelegramResponseException  as e:
            print(e) # do not handle error #403
    except Exception as e:
            print(e) # do not handle error #403
    except AssertionError:
            print( "!!!!!!! user has been blocked !!!!!!!" ) # do not handle error #403
     

tb.polling(none_stop=True, timeout=123)
    
bot.send_message(message.chat.id, '__Нижнее подчёркивание__', parse_mode='MarkdownV2')
bot.send_message(message.chat.id, '~Зачёркнутый~', parse_mode='MarkdownV2')

rom aiogram.utils.markdown import hlink

hello_with_url = hlink('Привет', 'https://pypi.org/project/pyTelegramBotAPI/#description')
bot.send_message(message.chat.id ,f'{hello_with_url}, я чат-бот ', reply_markup=markup,parse_mode='HTML')