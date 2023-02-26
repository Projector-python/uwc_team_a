import constants
from constants import bot, Student
from utils import build_inline_markup, build_reply_markup
from user_registration import procces_name
from user_update import procces_if_update

def user_panel_processing(message):
    if message.text == constants.REGISTRATION:
        student = Student()
        msg = bot.reply_to(message, "Привіт, ми почали реєстрацію. Напиши своє імʼя:")
        bot.register_next_step_handler(msg, procces_name, student = student)


    elif message.text == constants.UPDATE_PROFILE:
        # I need an instance Student from DB here
        student = Student()
        markup = build_reply_markup(constants.YES_NO)
        msg = bot.send_message(
            message.chat.id,
            student.overview + "\n Чи вам треба оновити дані про пошту, місце проживання, університет чи роботу?",
            reply_markup=markup
            )
        bot.register_next_step_handler(msg, procces_if_update, student = student)

    elif message.text == constants.UWC_SMM:
        markup = build_inline_markup(constants.SOCIAL_BUTTONS)

        bot.send_message(message.chat.id, "Our social media:",
                         reply_markup=markup)
