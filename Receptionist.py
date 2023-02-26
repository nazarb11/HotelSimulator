import random


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

    def choose_room(self, date):
        rooms = self.get_hotel().get_schedule().get_generated_list_of_rooms(date)
        for i in range(1, 100):
            number = random.randint(1, 10)
            if rooms[number]['availability']:
                return rooms[number]['number']
