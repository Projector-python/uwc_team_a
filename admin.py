import os

from telebot import types

import constants
from constants import bot
from db import db
from user_update import procces_if_update
from utils import build_reply_markup


def admin_panel_processing(message):
    if message.text == constants.ADD_ADMIN:
        msg = bot.send_message(
            message.chat.id, "Введіть ім'я нового адміна:"
        )
        bot.register_next_step_handler(msg, get_admin_id)

    elif message.text == constants.REMOVE_ADMIN:
        msg = bot.send_message(
            message.chat.id, "Введіть ID адміна, якого бажаєте видалити:"
        )
        bot.register_next_step_handler(msg, del_admin_from_db)

    elif message.text == constants.ADD_COLLEGE:
        msg = bot.send_message(
            message.chat.id, "Введіть коледж, який бажаєте додати:"
        )
        bot.register_next_step_handler(msg, process_college)

    elif message.text == constants.SEND_MESSAGE:
        markup = build_reply_markup(constants.SEND_MESSAGE_BUTTONS)

        msg = bot.send_message(
            message.chat.id, "Запит на оновлення чи інше повідомлення?",
            reply_markup=markup)
        bot.register_next_step_handler(msg, admin_send_message)

    elif message.text == constants.UWC_MEMBERS:
        # bot.send_document(message.chat.id, 'uwc_members.xlsx')
        pass

    elif message.text == constants.COLLEGES:
        # bot.send_document(message.chat.id, 'uwc_colleges.xlsx')
        pass

    elif message.text == constants.ADMINS:
        # bot.send_document(message.chat.id, 'uwc_admins.xlsx')
        pass


def get_admin_id(message):
    name = message.text
    msg = bot.send_message(message.chat.id, "Введіть ID нового адміна:")
    bot.register_next_step_handler(msg, add_admin_to_db, name=name)


def add_admin_to_db(message, name: str):
    telegram_id = message.text
    db.add_admin_to_db(telegram_id, name)
    bot.send_message(message.chat.id, "Адміна додано")


def del_admin_from_db(message):
    admin_id = message.text
    db.remove_admin_from_db(admin_id)
    bot.send_message(message.chat.id, "Адміна видалено")


def process_college(message):
    name = message.text
    msg = bot.send_message(
        message.chat.id, "Введіть локацію коледжу (нап. Європа:"
    )
    bot.register_next_step_handler(msg, add_college_to_db, name=name)


def add_college_to_db(message, name: str):
    college_location = message.text
    db.add_college_to_db(college_location, name)
    bot.send_message(message.chat.id, "Коледж додано")


def admin_send_message(message):
    if message.text == constants.UPDATE_DATA:
        markup = build_reply_markup(constants.YES_NO)

        for user in db.get_telegram_id_list():
            msg = bot.send_message(
                user, 'Привіт. Будь ласка оновіть дані вашого профілю',
                reply_markup=markup)
            bot.register_next_step_handler(msg, procces_if_update)
            # add update_date check and run update process if it need

        bot.reply_to(message, 'Done')

    elif message.text == constants.CUSTOM_MESSAGE:
        msg = bot.send_message(
            message.chat.id,
            "Напишіть повідомлення і воно буде надіслано всім учасникам:")
        bot.register_next_step_handler(
            msg, admin_send_custom_message_processing)


def admin_send_custom_message_processing(message):
    for user in db.get_telegram_id_list():
        bot.send_message(user, message.text)

    bot.reply_to(message, 'Повідомллення надіслані')


def admin_send_files_csv(message: types.Message, type: str):
    handler, filename = {
        'admins': (db.export_admins_to_csv, constants.FILE_ADMINS),
        'students': (db.export_student_to_csv, constants.FILE_STUDENTS),
        'colleges': (db.export_colleges_to_csv, constants.FILE_COLLEGES),
    }[type]

    handler()
    bot.send_document(message.from_user.id, filename)

    if os.path.exists(filename):
        os.remove(filename)
