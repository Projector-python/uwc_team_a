class Student:
    def __init__(self,
                 telegram_id: int = None,
                 name: str = None,
                 family_name: str = None,
                 college: str = None,
                 year_start: int = None,
                 year_finish: int = None,
                 email: str = None,
                 social_network: str = None,
                 best_commumication: str = None,
                 agree_share_pers_info: bool = None,
                 live_place: str = None,
                 university: str = None,
                 work: str = None,
                 interests: str = None,
                 date_updated=None):
        self.telegram_id = telegram_id
        self.name = name
        self.family_name = family_name
        self.college = college
        self.year_start = year_start
        self.year_finish = year_finish
        self.email = email
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

    def get_info(self) -> tuple:
        info = (
            self.telegram_id,
            self.name,
            self.family_name,
            self.college,
            self.year_start,
            self.year_finish,
            self.email,
            self.social_network,
            self.best_commumication,
            self.agree_share_pers_info,
            self.live_place,
            self.university,
            self.work,
            self.interests
        )

        return info
