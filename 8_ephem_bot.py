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

import ephem

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

planets = {
    'Mercury': ephem.Mercury(date.today()),
    'Venus': ephem.Venus(date.today()),
    # 'Earth': ephem.Earth(date.today()), 
    'Mars': ephem.Mars(date.today()), 
    'Jupiter': ephem.Jupiter(date.today()),
    'Saturn': ephem.Saturn(date.today()),
    'Uranus': ephem.Uranus(date.today()),
    'Neptune': ephem.Neptune(date.today()), 
    'Pluto': ephem.Pluto(date.today())
    }

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

  
def constellation(update, context):
    user_planet = update.message.text.split(' ')[1].capitalize()
    if user_planet in planets:
        update.message.reply_text(f'Планета в созвездии: {ephem.constellation(planets[user_planet])}')
    

def main():
    mybot = Updater("5167387084:AAHMbtEvAbZCVXpvcs0OkE4RhYRDolHtttE", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot Started')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
