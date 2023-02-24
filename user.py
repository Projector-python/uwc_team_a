import constants
from constants import bot
from utils import build_inline_markup


def user_panel_processing(message):
    if message.text == constants.REGISTRATION:
        pass    # Victor

    elif message.text == constants.UPDATE_PROFILE:
        pass

    elif message.text == constants.UWC_SMM:
        markup = build_inline_markup(constants.SOCIAL_BUTTONS)

        bot.send_message(message.chat.id, "Our social media:",
                         reply_markup=markup)
