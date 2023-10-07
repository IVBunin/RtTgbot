try:#обработка ошибок 
        bot.send_message(message.chat.id)
except ApiTelegramException as e:
    if e.description == "Forbidden: bot was blocked by the user":
        return 1  
        