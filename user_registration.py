from constants import bot
from db import db
from models import Student
from utils import check_str, check_int, check_email, \
    validate_str, validate_int, validate_mail


def process_name(message, student: Student):
    student.name = message.text
    if not check_str(student.name):
        bot.send_message(
            message.chat.id,
            """Ім'я введено невірно, використовуйте лише українську або \
                                англійську мову"""
        )
        return validate_str(message, student, process_name)
    ask_family_name(message, student=student)


def ask_family_name(message, student: Student):
    msg = bot.reply_to(message, "Напиши своє прізвище:")
    bot.register_next_step_handler(msg, process_family_name, student=student)


def process_family_name(message, student: Student):
    student.family_name = message.text
    if not check_str(student.family_name):
        bot.send_message(
            message.chat.id,
            """Прізвище введено невірно, спробуйте лише українську або \
                                англійську мову"""
        )
        return validate_str(message, student, process_family_name)
    ask_college(message, student=student)


def ask_college(message, student: Student):
    msg = bot.reply_to(message, "В якому коледжі ти навчався:")
    bot.register_next_step_handler(msg, process_college, student=student)


def process_college(message, student: Student):
    student.college = message.text
    ask_year_start(message, student=student)


def ask_year_start(message, student: Student):
    msg = bot.reply_to(message, "Напиши рік початку навчання (наприклад: 1999)")
    bot.register_next_step_handler(msg, process_year_start, student=student)


def process_year_start(message, student: Student):
    student.year_start = message.text
    if not check_int(student.year_start):
        bot.send_message(
            message.chat.id, "Рік введено невірно, використовуйте лише цифри"
        )
        return validate_int(message, student, process_year_start)
    ask_year_finish(message, student=student)


def ask_year_finish(message, student: Student):
    msg = bot.reply_to(message, "Напиши рік закінчення навчання (наприклад: 2001)")
    bot.register_next_step_handler(msg, process_year_finish, student=student)


def process_year_finish(message, student: Student):
    student.year_finish = message.text
    if not check_int(student.year_finish):
        bot.send_message(
            message.chat.id, "Рік введено невірно, використовуйте лише цифри"
        )
        return validate_int(message, student, process_year_finish)
    ask_mail(message, student=student)


def ask_mail(message, student: Student):
    msg = bot.reply_to(
        message,
        "Введи свою електронну пошту, наприклад name@gmail.com")
    bot.register_next_step_handler(msg, process_mail, student=student)


def process_mail(message, student: Student):
    student.mail = message.text
    if not check_email(student.mail):
        bot.send_message(
            message.chat.id,
            "Пошта вказана невірно, спробуйте знову, наприклад name@gmail.com"
        )
        return validate_mail(message, student, process_mail)
    ask_social_network(message, student=student)


def ask_social_network(message, student: Student):
    msg = bot.reply_to(message, "Введи свій ЛінкедІн, наприклад linkedIn/name")
    bot.register_next_step_handler(
        msg, process_social_network, student=student)


def process_social_network(message, student: Student):
    student.social_network = message.text
    ask_best_commumication(message, student=student)


def ask_best_commumication(message, student: Student):
    msg = bot.reply_to(
        message,
        "Введи зручний спосіб звʼязку, наприклад \"telegram: @name\"")
    bot.register_next_step_handler(
        msg, process_best_commumication, student=student)


def process_best_commumication(message, student: Student):
    student.best_commumication = message.text
    ask_agree_share_pers_info(message, student=student)


def ask_agree_share_pers_info(message, student: Student):
    msg = bot.reply_to(message, "Чи ти згодний на поширення особистих даних?")
    bot.register_next_step_handler(
        msg, process_agree_share_pers_info, student=student)


def process_agree_share_pers_info(message, student: Student):
    student.agree_share_pers_info = message.text
    ask_live_place(message, student=student)


def ask_live_place(message, student: Student):
    msg = bot.reply_to(message, "Де ти живеш? Наприклад, \"Київ, Україна\"")
    bot.register_next_step_handler(msg, process_live_place, student=student)


def process_live_place(message, student: Student):
    student.live_place = message.text
    ask_university(message, student=student)


def ask_university(message, student: Student):
    msg = bot.reply_to(message, """
        В якому університеті ти вчи-лась/вся? \
        Наприклад, \"Київський національний університет умені Тараса Шевченка\"
        """)
    bot.register_next_step_handler(msg, process_university, student=student)


def process_university(message, student: Student):
    student.university = message.text
    ask_work(message, student=student)


def ask_work(message, student: Student):
    msg = bot.reply_to(message, """
        Де та ким ти працюєш? /
        Наприклад \"Google, software engineer\"
        """)
    bot.register_next_step_handler(msg, process_work, student=student)


def process_work(message, student: Student):
    student.work = message.text
    ask_interests(message, student=student)


def ask_interests(message, student: Student):
    msg = bot.reply_to(message, "Які твої інтереси? Наприклад \"IT\"")
    bot.register_next_step_handler(msg, process_interests, student=student)


def process_interests(message, student: Student):
    student.interests = message.text
    bot.send_message(message.chat.id, "Дякую за реєстрацію!")
    student.telegram_id = message.from_user.id
    db.add_user_to_db(student)
