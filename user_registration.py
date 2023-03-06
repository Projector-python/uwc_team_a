from models import Student
from constants import bot
from db import db


def procces_name(message, student: Student):
    student.name = message.text
    ask_family_name(message, student=student)


def ask_family_name(message, student: Student):
    msg = bot.reply_to(message, "Напиши своє прізвище:")
    bot.register_next_step_handler(msg, procces_family_name, student=student)


def procces_family_name(message, student: Student):
    student.family_name = message.text
    ask_college(message, student=student)


def ask_college(message, student: Student):
    msg = bot.reply_to(message, "В якому коледжі ти навчався:")
    bot.register_next_step_handler(msg, procces_college, student=student)


def procces_college(message, student: Student):
    student.college = message.text
    ask_year_start(message, student=student)


def ask_year_start(message, student: Student):
    msg = bot.reply_to(message, "Напиши рік початку (наприклад: 1999)")
    bot.register_next_step_handler(msg, procces_year_start, student=student)


def procces_year_start(message, student: Student):
    student.year_start = message.text
    ask_year_finish(message, student=student)


def ask_year_finish(message, student: Student):
    msg = bot.reply_to(message, "Напиши рік кінця (наприклад: 2001)")
    bot.register_next_step_handler(msg, procces_year_finish, student=student)


def procces_year_finish(message, student: Student):
    student.year_finish = message.text
    ask_mail(message, student=student)


def ask_mail(message, student: Student):
    msg = bot.reply_to(
        message,
        "Введи свою електронну пошту, наприклад name@gmail.com")
    bot.register_next_step_handler(msg, procces_mail, student=student)


def procces_mail(message, student: Student):
    student.email = message.text
    ask_social_network(message, student=student)


def ask_social_network(message, student: Student):
    msg = bot.reply_to(message, "Введи свій ЛінкедІн, наприклад linkedIn/name")
    bot.register_next_step_handler(
        msg, procces_social_network, student=student)


def procces_social_network(message, student: Student):
    student.social_network = message.text
    ask_best_commumication(message, student=student)


def ask_best_commumication(message, student: Student):
    msg = bot.reply_to(
        message,
        "Введи зручний спосіб звʼязку, наприклад \"telegram: @name\"")
    bot.register_next_step_handler(
        msg, procces_best_commumication, student=student)


def procces_best_commumication(message, student: Student):
    student.best_commumication = message.text
    ask_agree_share_pers_info(message, student=student)


def ask_agree_share_pers_info(message, student: Student):
    msg = bot.reply_to(message, "Чи ти згодний на поширення особистих даних?")
    bot.register_next_step_handler(
        msg, procces_agree_share_pers_info, student=student)


def procces_agree_share_pers_info(message, student: Student):
    student.agree_share_pers_info = message.text
    ask_live_place(message, student=student)


def ask_live_place(message, student: Student):
    msg = bot.reply_to(message, "Де ти живеш? Наприклад, \"Київ, Україна\"")
    bot.register_next_step_handler(msg, procces_live_place, student=student)


def procces_live_place(message, student: Student):
    student.live_place = message.text
    ask_university(message, student=student)


def ask_university(message, student: Student):
    msg = bot.reply_to(message, """
        В якому університеті ти вчи-лась/вся? \
        Наприклад, \"Київський національний університет умені Тараса Шевченка\"
        """)
    bot.register_next_step_handler(msg, procces_university, student=student)


def procces_university(message, student: Student):
    student.university = message.text
    ask_work(message, student=student)


def ask_work(message, student: Student):
    msg = bot.reply_to(message, """
        Де та ким ти працюєш? /
        Наприклад \"Google, software engineer\"
        """)
    bot.register_next_step_handler(msg, procces_work, student=student)


def procces_work(message, student: Student):
    student.work = message.text
    ask_interests(message, student=student)


def ask_interests(message, student: Student):
    msg = bot.reply_to(message, "Які твої інтереси? Наприклад \"IT\"")
    bot.register_next_step_handler(msg, procces_interests, student=student)


def procces_interests(message, student: Student):
    student.interests = message.text
    bot.send_message(message.chat.id, "Дякую за реєстрацію!")
    student.telegram_id = message.from_user.id
    db.add_user_to_db(student)
