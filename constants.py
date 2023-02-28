import telebot
from models import College

TOKEN = '6172665923:AAFRPHtt2EIW0LLQYpGhk5l3F6bN3-2ZJAs'

bot = telebot.TeleBot(TOKEN)

DATABASE = 'uwc_database.db'

ADD_ADMIN = 'Add admin'
REMOVE_ADMIN = 'Remove admin'
SEND_MESSAGE = 'Send message to users'
UWC_MEMBERS = 'UWC Members'

REGISTRATION = 'Registration'
UPDATE_PROFILE = 'Update profile'
UWC_SMM = 'UWC Social Media'

UPDATE_DATA = 'Update data'
CUSTOM_MESSAGE = 'Custom message'

ADMIN_PANEL_BUTTONS = (
    ADD_ADMIN,
    REMOVE_ADMIN,
    SEND_MESSAGE,
    UWC_MEMBERS
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

colleges = [ 
            College("UWC Atlantic", "Europe"),
            College("UWC Dilijan", "Europe"),
            College("Li Po Chun UWC of Hong Kong", "Asia"),
            College("UWC Red Cross Nordic", "Europe"),
            College("UWC Maastricht", "Europe"),
            College("Pearson College UWC", "America"),
            College("UWC Robert Bosch College", "Europe"),
            College("UWC ISAK Japan", "Asia"),
            College("UWC Costa Rica", "America"),
            College("UWC Adriatic", "Europe"),
            College("UWC-USA", "America"),
            College("UWC Changshu China", "Asia"),
            College("UWC East Africa", "Africa"),
            College("UWC Thailand", "Asia"),
            College("Waterford Kamhlaba UWC of Southern Africa", "Africa"),
            College("UWC Mostar", "Europe"),
            College("UWC South East Asia", "Asia"),
            College("UWC Mahindra College", "Asia")
            ]