from telebot import types
import re
from constants import bot
from models import Student


def build_reply_markup(
        button_list: tuple[str],
        one_time_keyboard=True) -> types.ReplyKeyboardMarkup:

    markup = types.ReplyKeyboardMarkup(
        one_time_keyboard=one_time_keyboard,
        resize_keyboard=True,
        row_width=2
    )

    buttons = [types.KeyboardButton(i) for i in button_list]

    markup.add(*buttons)

    return markup


def build_inline_markup(
        button_list: dict[str, str]) -> types.InlineKeyboardButton:

    markup = types.InlineKeyboardMarkup(
        row_width=2
    )

    for button, url in button_list.items():
        markup.add(
            types.InlineKeyboardButton(button, url=url))

    return markup


def check_str(message):
    regex = (r"^[A-Za-zА-ЩЬЮЯҐЄІЇа-щьюяґєії' -]+$")
    pattern = re.compile(regex)
    match = pattern.search(message) is not None
    return match


def check_int(message):
    regex = (r"^[0-9]*$")
    pattern = re.compile(regex)
    match = pattern.search(message) is not None
    return match


def check_email(message):
    regex = (
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    )
    pattern = re.compile(regex)
    match = pattern.search(message) is not None
    return match


def validate_str(message, student: Student, func):
    return bot.register_next_step_handler(
        message, lambda message: func(message, student)
    )


def validate_int(message, student: Student, func):
    return bot.register_next_step_handler(
        message, lambda message: func(message, student)
    )


def validate_mail(message, student: Student, func):
    return bot.register_next_step_handler(
        message, lambda message: func(message, student)
    )
