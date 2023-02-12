import telebot
from config import TOKEN, admin_id
from telebot import types
bot = telebot.TeleBot(TOKEN)
from user_registration import *
student = Student()
# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    if message.text == '/start':
        mess = f'Hello, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text == '/help':
        bot.send_message(message.chat.id, "What bot can do?")

# Handle '/admin' for users with admin status
@bot.message_handler(commands=['admin'])
def admin_panel(message):
    if message.from_user.id in admin_id.values():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        # buttons:
        btn_1 = types.KeyboardButton('Website')
        btn_2 = types.KeyboardButton('UWC Members')
        btn_3 = types.KeyboardButton('Send message to users')
        btn_4 = types.KeyboardButton('Autentification', request_contact=True)

        markup.add(btn_1, btn_2, btn_3, btn_4)
        # markup.add(types.InlineKeyboardButton("Website", url= "https://www.ukraine.uwc.org")) # inline button
        bot.send_message(message.chat.id, "Hello! Welcome to admin panel!", reply_markup=markup)


# registration procces of a new student, using /register
@bot.message_handler(commands=["register"])
def ask_name(message):
    msg = bot.reply_to(message, "Привіт, ми почали реєстрацію. Напиши своє імʼя:")
    bot.register_next_step_handler(msg, procces_name)

def procces_name(message): 
    student.name = message.text
    ask_family_name(message)


def ask_family_name(message):
    msg = bot.reply_to(message, "Напиши своє прізвище:")
    bot.register_next_step_handler(msg, procces_family_name)

def procces_family_name(message):
    student.family_name = message.text
    ask_college(message)
    
def ask_college(message):
    msg = bot.reply_to(message, "В якому коледжі ти навчався:")
    bot.register_next_step_handler(msg, procces_college)

def procces_college(message):
    student.college = message.text
    ask_year_start(message)
    

def ask_year_start(message):
    msg = bot.reply_to(message, "Напиши рік початку (наприклад: 1999)")
    bot.register_next_step_handler(msg, procces_year_start)

def procces_year_start(message):
    student.year_start = message.text
    ask_year_finish(message)

def ask_year_finish (message):
    msg = bot.reply_to(message, f"Напиши рік кінця (наприклад: 2001)")
    bot.register_next_step_handler(msg, procces_year_finish)

def procces_year_finish(message):
    student.year_finish = message.text
    ask_mail(message)

def ask_mail(message):
    msg = bot.reply_to(message, f"Введи свою електронну пошту, наприклад name@gmail.com")
    bot.register_next_step_handler(msg, procces_mail)

def procces_mail(message):
    student.mail = message.text
    ask_social_network(message)

def ask_social_network(message):
    msg = bot.reply_to(message, f"Введи свій ЛінкедІн, наприклад linkedIn/name")
    bot.register_next_step_handler(msg, procces_social_network)

def procces_social_network(message):
    student.social_network = message.text
    ask_best_commumication(message)

def ask_best_commumication(message):
    msg = bot.reply_to(message, f"Введи зручний спосіб звʼязку, наприклад \"telegram: @name\"")
    bot.register_next_step_handler(msg, procces_best_commumication)

def procces_best_commumication(message):
    student.best_commumication = message.text
    ask_agree_share_pers_info(message)

def ask_agree_share_pers_info(message):
    msg = bot.reply_to(message, f"Чи ти згодний на поширення особистих даних?")
    bot.register_next_step_handler(msg, procces_agree_share_pers_info)

def procces_agree_share_pers_info (message):
    student.agree_share_pers_info = message.text
    ask_live_place(message)

def ask_live_place(message):
    msg = bot.reply_to(message, f"Де ти живеш? Наприклад, \"Київ, Україна\"")
    bot.register_next_step_handler(msg, procces_live_place)

def procces_live_place(message):
    student.live_place = message.text
    ask_university(message)

def ask_university(message):
    msg = bot.reply_to(message, f"В якому університеті ти вчи-лась/вся Наприклад, \"Київський національний університет умені Тараса Шевченка\"")
    bot.register_next_step_handler(msg, procces_university)

def procces_university(message):
    student.university = message.text
    ask_work(message)

def ask_work(message):
    msg = bot.reply_to(message, f"Де та ким ти працюєш? Наприклад \"Google, software engineer\"")
    bot.register_next_step_handler(msg, procces_work)

def procces_work(message):
    student.work = message.text
    ask_interests(message)

def ask_interests(message):
    msg = bot.reply_to(message, f"Які твої інтереси? Наприклад \"IT\"")
    bot.register_next_step_handler(msg, procces_interests)

def procces_interests (message):
    student.interests = message.text
    bot.send_message(message.chat.id, "Дякую за реєстрацію!")
    save_file(student)

def save_file(st: Student):
    import csv
    with open("users.csv", mode = "a") as file:
        writer = csv.writer (file)
        writer.writerow( [
            st.name,
            st.family_name,
            st.college,
            st.year_start,
            st.year_finish,
            st.mail,
            st.social_network,
            st.best_commumication,
            st.agree_share_pers_info,
            st.live_place,
            st.university,
            st.work,
            st.interests
        ]
        )
    
# handle any text from user
@bot.message_handler()
def message_reply(message):
    if message.text.capitalize() == 'Hello':
        bot.send_message(message.chat.id, 'Hello')
    elif message.text.upper() == 'ID':
        bot.send_message(message.chat.id, message.from_user.id)

bot.infinity_polling()