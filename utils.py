from telebot import types
import re

def build_reply_markup(
        button_list: tuple[str]) -> types.ReplyKeyboardMarkup:

    markup = types.ReplyKeyboardMarkup(
        one_time_keyboard=True,
        resize_keyboard=True,
        row_width=2
    )

    for button in button_list:
        markup.add(button)

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
    regex = (r"^[A-Za-zА-ЩЬЮЯҐЄІЇа-щьюяґєії'-]+$")
    pattern = re.compile(regex)
    match = pattern.search(message) is not None
    return match


def check_int(message):
    regex = (r"^[0-9]*$")
    pattern = re.compile(regex)
    match = pattern.search(message) is not None
    return match


def check_email(message):
    regex = (r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    pattern = re.compile(regex)
    match = pattern.search(message) is not None
    return match
