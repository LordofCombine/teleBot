import logging 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

# Настройки прокси
PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def hi_user(update,context):
    print('Вызван /start')
    update.message.reply_text('Привет, Человек! Ты вызвал команду /start')

#def calculator(update, context):
    #update.message.reply_text('Введите первое число: ')
    #a = int(input())
    #print(a)
    #update.message.reply_text('Что делать с ним будем? \n+ Сложим \n- Отнимем \n* Умножим \n/ Разделим \n** Возведём в степень \n% Корень из числа \n')
    #znak = input()
    #print(znak)
    #update.message.reply_text('Введите второе число: ')
    #print(b)
    #b = int(input())
    #if znak == '+':
    #    update.message.reply_text(a+b)
    #elif znak == '-':
    #    update.message.reply_text(a-b)
    #elif znak == '*':
    #    update.message.reply_text(a*b)
    #elif znak == '/':
    #    update.message.reply_text(a/b)
    #elif znak == '**':
    #    update.message.reply_text(a**b)
    #elif znak == '%':
    #    update.message.reply_text(a%b)
    #else:
    #    update.message.reply_text('Это калькулятор, а не записная книжка')
    
def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    
    dp = mybot.dispatcher

    dp.add_handler(CommandHandler("start", hi_user))
    #dp.add_handler(MessageHandler("cl", calculator))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    
    logging.info("Бот стартовал")
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()
    
def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)    

if __name__ == "__main__":
    main()