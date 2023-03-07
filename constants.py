import telebot

TOKEN = '6172665923:AAFRPHtt2EIW0LLQYpGhk5l3F6bN3-2ZJAs'

bot = telebot.TeleBot(TOKEN)

DATABASE = 'uwc_database.db'

ADD_ADMIN = 'Додати адміна'
REMOVE_ADMIN = 'Видалити адміна'
SEND_MESSAGE = 'Надіслати повідомлення учасникам'
UWC_MEMBERS = 'Інформація про учасників'
COLLEGES = 'Список коледжів'
ADMINS = 'Список адмінів'

REGISTRATION = 'Реєстрація'
UPDATE_PROFILE = 'Оновлення даних'
UWC_SMM = 'Соціальні мережі UWC'

UPDATE_DATA = 'Оновлення даних'
CUSTOM_MESSAGE = 'Інше повідомлення'

FILE_STUDENTS = 'uwc_students.csv'
FILE_COLLEGES = 'uwc_colleges.csv'
FILE_ADMINS = 'uwc_admins.csv'

YES = "Так"
NO = "Ніт"
YES_NO = (
    YES,
    NO
)

ADMIN_PANEL_BUTTONS = (
    ADD_ADMIN,
    REMOVE_ADMIN,
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
