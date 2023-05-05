import datetime


class Controller:
    def __init__(self, hotel, receptionist):
        self.__hotel = hotel
        self.__receptionist = receptionist

    def choice_stay(self, days, start_date):
        room_number = self.__receptionist.choose_room(start_date, days)
        if room_number == -1:
            return -1
        for day in range(0, days):
            self.__receptionist.check_in_room(room_number, start_date + datetime.timedelta(day))
