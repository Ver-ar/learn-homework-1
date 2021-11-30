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
from telegram import chat
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
  update.message.reply_text('Введи название планеты на английском языке') # не 
  print("Вызван /planet")

def find_planet(update, context):
  list_planet = [name for _0, _1, name in ephem._libastro.builtin_planets()] 
  planet = None
  text = update.message.text
  msg = text.lower().capitalize()
  print(msg)
  if msg in list_planet:
    planet = getattr(ephem, msg)(date.today())
  if planet is None and len(msg) < 9:
      update.message.reply_text('Извини, по этой планете у меня нет информации(')
  if len(msg) > 9:
    update.message.reply_text('ПЛА-НЕ-ТУ. НАЗ-ВА-НИ-Е.')
  else:
    planet_const = ephem.constellation(planet)
    update.message.reply_text(planet_const)

    


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