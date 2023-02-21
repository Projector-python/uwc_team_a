from telebot import types


def build_markup(button_list: tuple[str],
                 one_time_keyboard=True,
                 resize_keyboard=True,
                 row_width=2) -> types.ReplyKeyboardMarkup:

    markup = types.ReplyKeyboardMarkup(
        one_time_keyboard=one_time_keyboard,
        resize_keyboard=resize_keyboard,
        row_width=row_width
    )

    for button in button_list:
        markup.add(button)

    return markup
