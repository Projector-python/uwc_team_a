import telebot
from constants import TOKEN, admin_id
from telebot import types
from telebot.types import Message

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    if message.text == '/start':
        mess = f'Hello, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text == '/help':
        bot.send_message(message.chat.id, "What bot can do?")


@bot.message_handler(commands=['admin'])
def admin_panel(message: Message):
    if message.from_user.id in admin_id.values():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        admin_panel_buttons = [
            types.KeyboardButton('Website'),
            types.KeyboardButton('UWC Members'),
            types.KeyboardButton('Send message to users'),
            types.KeyboardButton('Autentification', request_contact=True)
        ]

        markup.add(admin_panel_buttons)
        bot.send_message(
            message.chat.id, "Hello! Welcome to admin panel!", reply_markup=markup)


@bot.message_handler()
def message_reply(message: Message):
    if message.text.capitalize() == 'Hello':
        bot.send_message(message.chat.id, 'Hello')
    elif message.text.upper() == 'ID':
        bot.send_message(message.chat.id, message.from_user.id)


bot.infinity_polling()
