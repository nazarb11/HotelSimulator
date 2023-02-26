import datetime


class Controller:
    def __init__(self, hotel, receptionist):
        self.__hotel = hotel
        self.__receptionist = receptionist

    def choice_stay(self, days):
        room_number = self.__receptionist.choose_room(datetime.date.today())
        for day in range(0, days):
            self.__receptionist.check_in_room(room_number, datetime.date.today() + datetime.timedelta(day))
