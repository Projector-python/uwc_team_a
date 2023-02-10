import telebot
from constants import TOKEN, admin_id
from telebot import types

bot = telebot.TeleBot(TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    if message.text == '/start':
        mess = f'Hello, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text == '/help':
        bot.send_message(message.chat.id, "What bot can do?")

# Handle '/admin' for users with admin status
@bot.message_handler(commands=['admin'])
def admin_panel(message):
    if message.from_user.id in admin_id.values():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        # buttons:
        btn_1 = types.KeyboardButton('Website')
        btn_2 = types.KeyboardButton('UWC Members')
        btn_3 = types.KeyboardButton('Send message to users')
        btn_4 = types.KeyboardButton('Autentification', request_contact=True)

        markup.add(btn_1, btn_2, btn_3, btn_4)
        # markup.add(types.InlineKeyboardButton("Website", url= "https://www.ukraine.uwc.org")) # inline button
        bot.send_message(message.chat.id, "Hello! Welcome to admin panel!", reply_markup=markup)

# handle any text from user
@bot.message_handler()
def message_reply(message):
    if message.text.capitalize() == 'Hello':
        bot.send_message(message.chat.id, 'Hello')
    elif message.text.upper() == 'ID':
        bot.send_message(message.chat.id, message.from_user.id)

bot.infinity_polling()