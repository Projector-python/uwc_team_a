import telebot

TOKEN = '6172665923:AAFRPHtt2EIW0LLQYpGhk5l3F6bN3-2ZJAs'

bot = telebot.TeleBot(TOKEN)

DATABASE = 'uwc_database.db'

BOT_INFO = """
    Цей бот створений для простішої комунікіції з \
    випускниками та студентами UWC. Він допоможе підтримувати \
    дані в актуальному стані.
"""

ADD_ADMIN = 'Додати адміна'
REMOVE_ADMIN = 'Видалити адміна'
ADD_COLLEGE = 'Додати коледж'
SEND_MESSAGE = 'Надіслати повідомлення учасникам'
UWC_MEMBERS = 'Список студентів'
COLLEGES = 'Список коледжів'
ADMINS = 'Список адмінів'

REGISTRATION = 'Реєстрація'
UPDATE_PROFILE = 'Оновлення даних'
UWC_SMM = 'Соціальні мережі UWC'

UPDATE_DATA = 'Запит на оновлення даних'
CUSTOM_MESSAGE = 'Інше повідомлення'

FILE_STUDENTS = 'uwc_students.csv'
FILE_COLLEGES = 'uwc_colleges.csv'
FILE_ADMINS = 'uwc_admins.csv'

UDPATE_REQUEST = """
    Привіт. Будь ласка оновіть дані вашого профілю, \
    якщо у вас були зміни пошти, місця роботи або проживання. \
    \nБажаєте змінити дані?
"""

YES = "Так"
NO = "Ніт"

YES_NO = (
    YES,
    NO
)

ADMIN_PANEL_BUTTONS = (
    ADD_ADMIN,
    REMOVE_ADMIN,
    ADD_COLLEGE,
    SEND_MESSAGE,
    UWC_MEMBERS,
    COLLEGES,
    ADMINS
)

USER_PANEL_BUTTONS = (
    REGISTRATION,
    UPDATE_PROFILE,
    UWC_SMM
)

SEND_MESSAGE_BUTTONS = (
    UPDATE_DATA,
    CUSTOM_MESSAGE
)

SOCIAL_BUTTONS = {
    'Instagram': 'https://www.instagram.com/uwcukraine',
    'Facebook': 'https://www.facebook.com/UWCUkraine',
    'Website': 'https://www.ukraine.uwc.org',
    'LinkedIn': 'https://www.linkedin.com/company/uwcukraine'
}

LOCATIONS = (
    'Asia',
    'Africa',
    'America',
    'Europe'
)
