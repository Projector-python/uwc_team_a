import telebot

TOKEN = '6172665923:AAFRPHtt2EIW0LLQYpGhk5l3F6bN3-2ZJAs'

bot = telebot.TeleBot(TOKEN)

database = 'uwc_database.db'

admin_panel_buttons = (
    'Add admin',
    'Remove admin',
    'Send message to users',
    'UWC Members'
)

user_panel_buttons = (
    'Registration',
    'Update profile',
    'UWC Social Media'
)

send_message_buttons = (
    'Update data',
    'Custom message'
)
