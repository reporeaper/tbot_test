import random
import telebot
from bot_api import bot_token
from telebot import types

token = bot_token

bot = telebot.TeleBot(token)

options = ["Орел", "Решка", "Ребро"]

@bot.message_handler(commands=['start'])
def handle_start(message):

    keyboard = types.ReplyKeyboardMarkup(True)
    button1 = types.KeyboardButton("Орел")
    button2 = types.KeyboardButton("Решка")
    button3 = types.KeyboardButton("Ребро")
    keyboard.add(button1, button2, button3)

    bot.send_message(message.chat.id, "Привет! Я бот для игры в монетку. Подбрось и узнай, повезло тебе или нет.", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_message(message):

    random_object = random.choice(options)
    result = "Ничья. Подбрось еще раз"

    if message.text == "Орел" and random_object == "Решка":
        result = "Не повезло"
    elif message.text == "Орел" and random_object == "Орел":
        result = "Повезло"
    elif message.text == "Орел" and random_object == "Ребро":
        result = "Ничья. Подбрось еще раз"

    elif message.text == "Решка" and random_object == "Орел":
        result = "Не повезло"
    elif message.text == "Решка" and random_object == "Решка":
        result = "Повезло"
    elif message.text == "Решка" and random_object == "Ребро":
        result = "Ничья. Подбрось еще раз"

    elif message.text == "Ребро" and random_object == "Ребро":
        result = "Повезло"
    elif message.text == "Ребро" and random_object == "Орел":
        result = "Не повезло"
    elif message.text == "Ребро" and random_object == "Решка":
        result = "Не повезло"

    bot.send_message(message.chat.id, random_object)
    bot.reply_to(message, result)

bot.polling(non_stop=True)




# @bot.message_handler(commands=['start'])
# def handle_start(message):
#     bot.send_message(message.chat.id, "Привет! Я бот для игры в Flip A Coin. Напиши /flip, чтобы подбросить монетку.")
#
# @bot.message_handler(commands=['flip'])
# def handle_flip(message):
#     result = random.choice(['Орел', 'Решка', 'Ребро'])
#     bot.send_message(message.chat.id, f"Выпало: {result}")
#
# bot.polling(none_stop = True)