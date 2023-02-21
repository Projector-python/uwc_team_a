import telebot
import constants
from constants import bot
from telebot import types
from telebot.types import Message


def build_markup(button_list: tuple):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                       resize_keyboard=True, row_width=2)

    for button in button_list:
        markup.add(button)

    return markup
