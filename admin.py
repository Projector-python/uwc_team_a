import constants
from constants import bot
from utils import build_reply_markup
from db import db


def admin_panel_processing(message):
    if message.text == constants.ADD_ADMIN:
        msg = bot.send_message(
            message.chat.id, "Введіть ім'я нового адміна:"
        )
        bot.register_next_step_handler(msg, get_admin_id)

    elif message.text == constants.REMOVE_ADMIN:
        msg = bot.send_message(
            message.chat.id, "Введіть ID адміна, якого бажаєте видалити:"
        )
        bot.register_next_step_handler(msg, del_admin_from_db)

    elif message.text == constants.SEND_MESSAGE:
        markup = build_reply_markup(constants.SEND_MESSAGE_BUTTONS)

        msg = bot.send_message(
            message.chat.id, "Update data request or custom message?",
            reply_markup=markup)
        bot.register_next_step_handler(msg, admin_send_message)

    elif message.text == constants.UWC_MEMBERS:
        pass


def get_admin_id(message):
    name = message.text
    msg = bot.send_message(message.chat.id, "Введіть ID нового адміна:")
    bot.register_next_step_handler(msg, add_admin_to_db, name=name)


def add_admin_to_db(message, name: str):
    telegram_id = message.text
    db.add_admin_to_db(telegram_id, name)
    bot.send_message(message.chat.id, "Адміна додано")


def del_admin_from_db(message):
    admin_id = message.text
    db.remove_admin_from_db(admin_id)
    bot.send_message(message.chat.id, "Адміна видалено")


def admin_send_message(message):
    if message.text == constants.UPDATE_DATA:
        for user in db.get_telegram_id_list():
            bot.send_message(user, 'Please update your profile')

        bot.reply_to(message, 'Done')

    elif message.text == constants.CUSTOM_MESSAGE:
        msg = bot.send_message(
            message.chat.id, "Write the message for all UWC members:")
        bot.register_next_step_handler(
            msg, admin_send_custom_message_processing)


def admin_send_custom_message_processing(message):
    for user in db.get_telegram_id_list():
        bot.send_message(user, message.text)

    bot.reply_to(message, 'Done')
