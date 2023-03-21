class Hotel:
    def __init__(self, name, rooms_number, receptionist, rooms, schedule):
        self.__name = name
        self.__rooms_number = rooms_number
        self.__receptionist = receptionist
        self.__rooms = rooms
        self.__schedule = schedule

    def check_in_room(self, room_number, date):
        rooms = self.get_rooms(date)
        for room in rooms:
            if room['number'] == room_number:
                room['availability'] = False
                break

    def check_out_room(self, room_number, date):
        rooms = self.get_rooms(date)
        for room in rooms:
            if room['number'] == room_number:
                room['availability'] = True
                self.update_rooms_schedule(rooms, date)
                break

    def is_free_room(self, room_number, date):
        rooms = self.get_rooms(date)
        for room in rooms:
            if room['number'] == room_number:
                return room['availability']

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_rooms_number(self, rooms_number):
        self.__rooms_number = rooms_number

    def get_rooms_number(self):
        return self.__rooms_number

    def set_receptionist(self, receptionist):
        self.__receptionist = receptionist

    def get_receptionist(self):
        return self.__receptionist

    def set_rooms(self, rooms):
        self.__rooms = rooms

    def get_rooms(self, date):
        return self.__rooms[str(date)]

    def update_dates_schedule(self, updated_schedule):
        self.__schedule.set_list_of_dates(updated_schedule)

    def update_rooms_schedule(self, updated_schedule, _date):
        dates = self.__schedule.get_generated_list_of_dates()
        for date in dates:
            if date == str(_date):
                self.__schedule.set_list_of_rooms(updated_schedule, _date)

    def get_schedule(self):
        return self.__schedule
