from telebot import types


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
