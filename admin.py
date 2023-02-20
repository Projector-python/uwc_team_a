import telebot
from constants import bot
from telebot import types
from telebot.types import Message
import db


def admin_panel_processing(message):
    if message.text == 'Add admin':
        pass    # Eugene

    elif message.text == 'Remove admin':
        pass    # Eugene

    elif message.text == 'Send message to users':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
            resize_keyboard=True, row_width=2,)

        buttons = [
            types.KeyboardButton('Update data'),
            types.KeyboardButton('Custom message')
        ]

        markup.add(*buttons)
        msg = bot.send_message(
            message.chat.id, "Update data request or custom message?", 
                reply_markup=markup)
        bot.register_next_step_handler(msg, admin_send_message)

    elif message.text == 'UWC Members':
        pass
    

def admin_send_message(message):
    if message.text == 'Update data':
        msg = 'Please update your profile'
        for user in db.get_user_id_list():
            bot.send_message(user, msg)
        bot.reply_to(message, 'Done')

    elif message.text == 'Custom message':
        msg = bot.send_message(
            message.chat.id, "Write the message for all UWC members:")
        bot.register_next_step_handler(
            msg, admin_send_custom_message_processing)


def admin_send_custom_message_processing(message):
    for user in db.get_user_id_list():
        bot.send_message(user, message.text)
    bot.reply_to(message, 'Done')
    