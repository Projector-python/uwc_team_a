import constants
from constants import bot
from models import Student
from utils import build_inline_markup
from user_registration import procces_name


def user_panel_processing(message):
    if message.text == constants.REGISTRATION:
        student = Student()
        msg = bot.reply_to(
            message, "Привіт, ми почали реєстрацію. Напиши своє імʼя:")
        bot.register_next_step_handler(msg, procces_name, student=student)

    elif message.text == constants.UPDATE_PROFILE:
        pass

    elif message.text == constants.UWC_SMM:
        markup = build_inline_markup(constants.SOCIAL_BUTTONS)

        bot.send_message(message.chat.id, "Our social media:",
                         reply_markup=markup)
