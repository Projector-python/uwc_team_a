import telebot

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

class College:
    def __init__(self, name, region) -> None:
        self.name = name
        self.region = region

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

class Student:
    def __init___(self, 
                    telegram_id: int,
                    name: str, 
                    family_name: str,
                    college: College,
                    year_start: int,
                    year_finish: int,
                    mail: str,
                    social_network: str,
                    best_commumication: str,
                    agree_share_pers_info: bool,
                    live_place: str,
                    university: str,
                    work: str,
                    interests: str,
                    date_updated):
        self.telegram_id = telegram_id
        self.name = name 
        self.family_name = family_name
        self.college = college
        self.year_start = year_start
        self.year_finish = year_finish
        self.mail = mail
        self.social_network = social_network
        self.best_commumication = best_commumication
        self.agree_share_pers_info = agree_share_pers_info
        self.live_place = live_place
        self.university = university
        self.work = work
        self.interests = interests
        self.date_updated = date_updated
        
        @property
        def overview(self):
            return f"""
            Мене звати {self.name} {self.family_name}
            Коледж  {self.college.name}, {self.year_start}-{self.year_finish}
            Пошта  {self.email}
            Соц-мережа  {self.social_network}, найркаще комунікувати {self.best_communication}
            Живу в {self.live_place}
            Університет {self.university}
            Робота {self.work}
            Інтереси {self.interests}
            Востаннє оновлюваллись дані {self.date_updated}
            """

