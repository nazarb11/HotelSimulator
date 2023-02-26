class Room:
    def __init__(self, number, availability, price):
        self.availability = availability
        self.number = number
        self.price = price
        self.dates = []

    def print_all(self):
        print(f'Room number: {self.number}\n'
              f'Status: {self.availability}')

    def check_in_room(self):
        self.availability = False

    def check_out_room(self):
        self.availability = True

    def get_availability(self):
        return self.availability
