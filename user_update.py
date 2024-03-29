import constants
from constants import bot
from db import db
from models import Student
from utils import build_reply_markup


def procces_if_update(message):
    if (message.text == constants.NO):
        db.refresh_update_date(message.from_user.id)
    elif (message.text == constants.YES):
        student = db.get_student_info(message.from_user.id)
        markup = build_reply_markup(["Далі"])
        msg = bot.send_message(
            message.chat.id,
            """Ми пройдемось по кожному з параметрів та змінимо їх за необхідності. Натиснііть кнопку \"Далі\" щоб почати :)""",
            reply_markup=markup
        )
        bot.register_next_step_handler(msg, ask_change_mail, student)


def ask_change_mail(message, student: Student):
    markup = build_reply_markup(constants.YES_NO)
    msg = bot.send_message(
        message.chat.id,
        f"Ваша пошта {student.email}. Треба її змінити?",
        reply_markup=markup
    )
    bot.register_next_step_handler(msg, procces_if_change_mail, student)


def procces_if_change_mail(message, student: Student):
    if message.text == constants.YES:
        msg = bot.send_message(
            message.chat.id,
            "Введіть нову електронну пошту:"
        )
        bot.register_next_step_handler(
            msg, procces_change_mail, student=student
        )
    elif message.text == constants.NO:
        ask_change_live_place(message, student)


def procces_change_mail(message, student: Student):
    student.email = message.text
    ask_change_mail(message, student)


def ask_change_live_place(message, student: Student):
    markup = build_reply_markup(constants.YES_NO)
    msg = bot.send_message(
        message.chat.id,
        f"Ви живете в {student.live_place}. Треба змінити інформацію?",
        reply_markup=markup
    )
    bot.register_next_step_handler(msg, procces_if_change_live_place, student)


def procces_if_change_live_place(message, student: Student):
    if message.text == constants.YES:
        msg = bot.send_message(message.chat.id,
                               "Введіть нове місце проживання:")
        bot.register_next_step_handler(
            msg, procces_change_live_place, student=student)
    elif message.text == constants.NO:
        ask_change_work(message, student)


def procces_change_live_place(message, student: Student):
    student.live_place = message.text
    ask_change_live_place(message, student)


def ask_change_work(message, student: Student):
    markup = build_reply_markup(constants.YES_NO)
    msg = bot.send_message(
        message.chat.id,
        f"Ваша робота \"{student.work}\". Треба змінити інформацію?",
        reply_markup=markup,
    )
    bot.register_next_step_handler(msg, procces_if_change_work, student)


def procces_if_change_work(message, student: Student):
    if message.text == constants.YES:
        msg = bot.send_message(
            message.chat.id,
            "Введіть місце роботи:",
        )
        bot.register_next_step_handler(
            msg, procces_change_work, student=student,
        )
    elif message.text == constants.NO:
        ask_change_university(message, student)


def procces_change_work(message, student: Student):
    student.work = message.text
    ask_change_work(message, student)


def ask_change_university(message, student: Student):
    markup = build_reply_markup(constants.YES_NO)
    msg = bot.send_message(
        message.chat.id,
        f"Ваш університет \"{student.university}\". Треба змінити інформацію?",
        reply_markup=markup
    )
    bot.register_next_step_handler(msg, procces_if_change_university, student)


def procces_if_change_university(message, student: Student):
    if message.text == constants.YES:
        msg = bot.send_message(
            message.chat.id,
            "Введіть університет:"
        )
        bot.register_next_step_handler(
            msg, procces_change_university, student=student
        )
    elif message.text == constants.NO:
        save_info(message, student)


def procces_change_university(message, student: Student):
    student.university = message.text
    ask_change_university(message, student)


def save_info(message, student: Student):
    db.update_user_in_db(student)

    markup = build_reply_markup(
        constants.USER_PANEL_BUTTONS, one_time_keyboard=False)
    bot.send_message(
        message.chat.id, "Дякую, ваші дані оновлено!", reply_markup=markup)
