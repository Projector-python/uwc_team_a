import telebot
from constants import bot
from telebot import types
from telebot.types import Message
from utils import build_markup
from db import db


def user_panel_processing(message):
    if message.text == 'Registration':
        pass    # Victor

    elif message.text == 'Update profile':
        pass

    elif message.text == 'UWC Social Media':
        markup = types.InlineKeyboardMarkup(row_width=2)

        social_buttons = [
            types.InlineKeyboardButton('Instagram',
                            url='https://www.instagram.com/uwcukraine'),
            types.InlineKeyboardButton('Facebook',
                            url='https://www.facebook.com/UWCUkraine'),
            types.InlineKeyboardButton('Website',
                            url='https://www.ukraine.uwc.org'),
            types.InlineKeyboardButton('LinkedIn',
                            url='https://www.linkedin.com/company/uwcukraine')
        ]

        markup.add(*social_buttons)
        bot.send_message(message.chat.id, "Our social media:",
                         reply_markup=markup)
