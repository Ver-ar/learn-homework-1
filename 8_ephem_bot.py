"""
Домашнее задание №1
Использование библиотек: ephem
* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.
"""
import logging
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
from datetime import date

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text("Привет! С помощью меня ты можешь узнать в каком созвездии сегодня находится интересующая тебя планета! Набери: /planet")




def get_planet(update, context):
    print("Вызван /planet")
    update.message.reply_text('Введи название планеты на английском языке') # не понимаю как отсюда передается сообщение пользователя в функцию find_planet, 
    #просто как аргумент к переменной update.message.text после ввода update.message.reply_text, потому что такая функция введена в модуле телеграм?

def find_planet(update, context):
    list_planet = [ephem._libastro.builtin_planets()]
    text = update.message.text
    if text in list_planet:
      planet = getattr(ephem, text) 
      planet_const = ephem.constellation(planet)
      update.message.reply_text(planet_const)
    else:
      update.message.reply_text('Извини, по этой планете у меня нет информации(')
    


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet))    
    dp.add_handler(MessageHandler(Filters.text, find_planet))
    mybot.start_polling()
    mybot.idle()



if __name__ == "__main__":
    main()