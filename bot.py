#!/usr/bin/env python

#TODO
# 1) разабрацца з Git
# 2) деплой на Heroku
# 3) разабрацца з SQLite
# 4) тест бот-нагадвальнік
# 5) бот-слоўнік з дадатковым функцыяналам гульні-карткі са словамі

import random

import telebot
from telebot.types import Message

# bot token
TOKEN = '5339522966:AAEGlvuO7I6jRuQ_wRI_wwSC422WMYxKTE8'
STICKER_ID = 'CAACAgQAAxkBAAMTYoP_6JfQZVW2hZyiOSb5MUX4tNAAAogGAAJRjM8BvORQjF7kUHokBA'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def command_start(message: Message):
    bot.reply_to(message, 'Command is start')


@bot.message_handler(commands=['help'])
def command_help(message: Message):
    bot.reply_to(message, 'Command is help')


@bot.message_handler(content_types=['text'])
def echo_name(message: Message):
    if message.from_user.full_name == 'Я':
        bot.reply_to(message, f'Прывітанне, спадар {message.from_user.full_name}!')
    else:
        bot.send_sticker(message.chat.id, STICKER_ID)


bot.polling()
