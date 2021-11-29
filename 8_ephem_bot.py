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
    update.message.reply_text("Привет! С помощью меня ты можешь узнать в каком созвездии сегодня находится интересующая тебя планета! Набери: /planet planetname")




def ephem_planet(update, context):
    text = update.message.text
    today = str(date.today())
    message = text.lower().split()
    star = message[1]
    star = star.capitalize()    
    if star in ephem._libastro.builtin_planets():
      print(star)


    


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    
    dp.add_handler(CommandHandler("planet", ephem_planet))
    mybot.start_polling()
    mybot.idle()



if __name__ == "__main__":
    main()



    ____________________________


planet = input()
a = 5
planets = [(0, 'Planet', 'Mercury'), 
(1, 'Planet', 'Venus'), (2, 'Planet', 'Mars'), (3, 'Planet', 'Jupiter'), 
(4, 'Planet', 'Saturn'), (5, 'Planet', 'Uranus'), (6, 'Planet', 'Neptune'), 
(7, 'Planet', 'Pluto'), (8, 'Planet', 'Sun'), (9, 'Planet', 'Moon'), 
(10, 'PlanetMoon', 'Phobos'), (11, 'PlanetMoon', 'Deimos'), 
(12, 'PlanetMoon', 'Io'), (13, 'PlanetMoon', 'Europa'), 
(14, 'PlanetMoon', 'Ganymede'), (15, 'PlanetMoon', 'Callisto'), 
(16, 'PlanetMoon', 'Mimas'), (17, 'PlanetMoon', 'Enceladus'), 
(18, 'PlanetMoon', 'Tethys'), (19, 'PlanetMoon', 'Dione'), 
(20, 'PlanetMoon', 'Rhea'), (21, 'PlanetMoon', 'Titan'), 
(22, 'PlanetMoon', 'Hyperion'), (23, 'PlanetMoon', 'Iapetus'), 
(24, 'PlanetMoon', 'Ariel'), (25, 'PlanetMoon', 'Umbriel'), 
(26, 'PlanetMoon', 'Titania'), (27, 'PlanetMoon', 'Oberon'), 
(28, 'PlanetMoon', 'Miranda')]

if planet in planets:
    print(a)