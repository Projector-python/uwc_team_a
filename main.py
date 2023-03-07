import constants
import admin
import user
from constants import bot
from telebot.types import Message
from utils import build_reply_markup
from db import db


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    if message.text == '/start':
        mess = f'Привіт, <b>{message.from_user.first_name}</b>'
        markup = build_reply_markup(constants.USER_PANEL_BUTTONS)

        msg = bot.send_message(message.chat.id, mess,
                               parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg, user.user_panel_processing)

    elif message.text == '/help':
        bot.send_message(message.chat.id, "What bot can do?")


@bot.message_handler(commands=['admin'])
def admin_panel(message: Message):
    if db.is_admin(message.from_user.id):
        markup = build_reply_markup(constants.ADMIN_PANEL_BUTTONS)

        msg = bot.send_message(
            message.chat.id, "Привіт. Ви знаходитесь в адмін панелі!",
            reply_markup=markup)
        bot.register_next_step_handler(msg, admin.admin_panel_processing)


@bot.message_handler()
def message_reply(message: Message):
    if message.text.upper() == 'ID':
        bot.send_message(message.chat.id, message.from_user.id)


bot.infinity_polling()
