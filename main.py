import telebot
from constants import bot
from telebot import types
from telebot.types import Message
import admin, user, db


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    if message.text == '/start':
        mess = f'Hello, <b>{message.from_user.first_name}</b>'
        db.add_user_id(message.from_user.id)    # add new user_id to all_users

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

        user_panel_buttons = [
            types.KeyboardButton('Registration'),
            types.KeyboardButton('Update profile'),
            types.KeyboardButton('UWC Social Media')
        ]

        markup.add(*user_panel_buttons)
        msg = bot.send_message(message.chat.id, mess,
                               parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg, user.user_panel_processing)

    elif message.text == '/help':
        bot.send_message(message.chat.id, "What bot can do?")


@bot.message_handler(commands=['admin'])
def admin_panel(message: Message):
    if db.is_admin(message.from_user.id):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        admin_panel_buttons = [
            types.KeyboardButton('Add admin'),
            types.KeyboardButton('Remove admin'),
            types.KeyboardButton('Send message to users'),
            types.KeyboardButton('UWC Members')
        ]

        markup.add(*admin_panel_buttons)
        msg = bot.send_message(
            message.chat.id, "Hello! Welcome to admin panel!",
            reply_markup=markup)
        bot.register_next_step_handler(msg, admin.admin_panel_processing)


@bot.message_handler()
def message_reply(message: Message):
    if message.text.upper() == 'ID':
        bot.send_message(message.chat.id, message.from_user.id)


bot.infinity_polling()
