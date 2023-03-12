import constants
from constants import bot
from models import Student
from user_registration import process_name
from user_update import procces_if_update
from utils import build_inline_markup, build_reply_markup
from db import db


def user_panel_processing(message):
    if message.text == constants.REGISTRATION:
        if db.is_user(message.from_user.id):
            bot.reply_to(
            message, "Ви вже реєструвались, спробуйте оновити свої дані")
        else:
            student = Student()
            msg = bot.reply_to(
                message, "Привіт, ми почали реєстрацію. Напиши своє імʼя:")
            bot.register_next_step_handler(msg, process_name, student=student)

    elif message.text == constants.UPDATE_PROFILE:
        markup = build_reply_markup(constants.YES_NO)

        msg = bot.reply_to(
            message, f"""Ви хочете оновити свої дані? \n
            {db.get_student_info(message.from_user.id).overview}""",
            reply_markup=markup
        )
        bot.register_next_step_handler(
            msg, procces_if_update)

    elif message.text == constants.UWC_SMM:
        markup = build_inline_markup(constants.SOCIAL_BUTTONS)

        bot.send_message(message.chat.id, "Наші соціальні мережі:",
                         reply_markup=markup)
