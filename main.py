from telebot.types import Message
import constants
import user
from constants import bot
from utils import build_reply_markup


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    if message.text == '/start':
        mess = f'Привіт, <b>{message.from_user.first_name}</b>'
        markup = build_reply_markup(
            constants.USER_PANEL_BUTTONS, one_time_keyboard=False)

        msg = bot.send_message(message.chat.id, mess,
                               parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg, user.user_panel_processing)

    elif message.text == '/help':
        bot.send_message(message.chat.id, constants.BOT_INFO)


@bot.message_handler()
def message_reply(message: Message):
    if message.text.upper() == 'ID':
        bot.send_message(message.chat.id, message.from_user.id)


bot.infinity_polling()
