import random
import datetime
from copy import copy


class Receptionist:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__hotel = None

    def print_all(self):
        print(f'Name: {self.name}\n'
              f'Age: {self.age}')

    def check_in_room(self, room_number, date):
        if self.check_if_room_is_available(room_number, date):
            self.get_hotel().check_in_room(room_number, date)
            print(f'Room number {room_number} is booked for {str(date)}')
        else:
            print(f'Room number {room_number} is not free for {str(date)}')

    def set_hotel(self, hotel):
        self.__hotel = hotel

    def get_hotel(self):
        if self.__hotel:
            return self.__hotel

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def check_if_room_is_available(self, room_number, date):
        return self.get_hotel().is_free_room(room_number, date)

    def choose_room(self, date, days):
        room_number = -1
        day = 0
        all_rooms = list()
        for room in self.get_hotel().get_rooms(str(date)):
            all_rooms.append(room['number'])
        while day < days:
            rooms = self.get_hotel().get_schedule().get_generated_list_of_rooms(date + datetime.timedelta(day))
            if room_number == -1:
                for i in range(0, 100):
                    number = all_rooms[random.randint(1, len(all_rooms)) - 1]
                    try:
                        if not rooms[number - 1]['availability']:
                            for el in all_rooms:
                                if el == rooms[number - 1]['number']:
                                    all_rooms.pop(number)
                                    if len(all_rooms) == 0:
                                        print('No rooms available for selected amount of days')
                                        return -1
                        else:
                            room_number = number
                            day = day + 1
                            break
                    except IndexError:
                        print('Error')
            else:
                try:
                    if not rooms[room_number - 1]['availability']:
                        for el in all_rooms:
                            if el == room_number:
                                all_rooms.pop(room_number)
                                if len(all_rooms) == 0:
                                    print('No rooms available for selected amount of days')
                                    return -1
                                break
                        room_number = -1
                        day = 0
                    else:
                        day = day + 1
                except IndexError:
                    print('Error')

        return room_number
