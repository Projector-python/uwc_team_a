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
    # def __init__(self) -> None:
    #     self.type = "human"

    def __init___(self, 
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
                    interests: str):
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
