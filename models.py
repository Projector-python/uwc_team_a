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
                 best_communication: str = None,
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
        self.best_communication = best_communication
        self.agree_share_pers_info = agree_share_pers_info
        self.live_place = live_place
        self.university = university
        self.work = work
        self.interests = interests
        self.date_updated = date_updated

    @property
    def overview(self):
        return f"""Профіль студента: \n
        \nМене звати {self.name} \
        \nКоледж  {self.college}, {self.year_start}-{self.year_finish} \
        \nПошта  {self.email} \
        \nСоц-мережа  {self.social_network}, найкраще комунікувати {self.best_communication} \
        \nЖиву в {self.live_place} \
        \nУніверситет {self.university} \
        \nРобота {self.work} \
        \nІнтереси {self.interests} \
        \nВостаннє оновлюваллись дані {self.date_updated}
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
            self.best_communication,
            self.agree_share_pers_info,
            self.live_place,
            self.university,
            self.work,
            self.interests
        )

        return info
