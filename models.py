class Student:
    def __init___(self,
                  telegram_id: int,
                  name: str,
                  family_name: str,
                  college: str,
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
        Коледж  {self.college}, {self.year_start}-{self.year_finish}
        Пошта  {self.email}
        Соц-мережа  {self.social_network}, \
        найркаще комунікувати {self.best_communication}
        Живу в {self.live_place}
        Університет {self.university}
        Робота {self.work}
        Інтереси {self.interests}
        Востаннє оновлюваллись дані {self.date_updated}
        """
