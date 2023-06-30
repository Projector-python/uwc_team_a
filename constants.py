import telebot

# TOKEN =

bot = telebot.TeleBot(TOKEN)

DATABASE = 'uwc_database.db'

BOT_INFO = """Цей бот створений для простішої комунікіції з \
    випускниками та студентами UWC. Він допоможе підтримувати \
    дані в актуальному стані.
    """

CANCEL = 'Назад'

ADD_ADMIN = 'Додати адміна'
REMOVE_ADMIN = 'Видалити адміна'
ADD_COLLEGE = 'Додати коледж'
SEND_MESSAGE = 'Повідомлення учасникам'
UWC_MEMBERS = 'Список студентів'
COLLEGES = 'Список коледжів'
ADMINS = 'Список адмінів'

REGISTRATION = 'Реєстрація'
PROFILE = 'Профіль студента'
UPDATE_PROFILE = 'Оновлення даних'
UWC_SMM = 'Соціальні мережі UWC'
ADMIN_PANEL = 'Панель адміністратора'

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

REGISTRATION_ASK = """
    Здається ви ще не зареєстровані як студент, або випускник \
    UWC. Ви можете зробити це, натиснувши "реєстрація" в \
    головному меню.
"""

YES = "Так"
NO = "Ні"

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
    PROFILE,
    UPDATE_PROFILE,
    UWC_SMM,
    ADMIN_PANEL
)

SEND_MESSAGE_BUTTONS = (
    UPDATE_DATA,
    CUSTOM_MESSAGE,
    CANCEL
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
