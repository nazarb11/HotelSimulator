import json
import random
import datetime


class Schedule:
    def __init__(self, rooms_number, days_to_generate, lowest_room_price_threshold, highest_room_price_threshold):
        with open('schedule.json', 'r') as schedule_json:
            self.generated_list_of_dates = json.load(schedule_json)
        self.generated_list_of_rooms = list()

        for day in range(0, days_to_generate):
            self.generated_list_of_rooms.clear()
            for room in range(1, rooms_number + 1):
                new_room = {'number': room,
                            'price': random.randint(lowest_room_price_threshold, highest_room_price_threshold),
                            'availability': True
                            }
                self.generated_list_of_rooms.append(new_room)
            new_day = {str(datetime.date.today() + datetime.timedelta(days=day)): self.generated_list_of_rooms}
            self.generated_list_of_dates.update(new_day)

        with open('schedule.json', 'w') as schedule_json:
            json.dump(self.generated_list_of_dates, schedule_json, indent=4)

    def get_generated_list_of_dates(self):
        return self.generated_list_of_dates

    def get_generated_list_of_rooms(self, date):
        return self.get_generated_list_of_dates()[str(date)]

    def set_list_of_dates(self, updated_list):
        self.generated_list_of_dates = updated_list

    def set_list_of_rooms(self, updated_list, _date):
        dates = self.get_generated_list_of_dates()
        for date in dates:
            if date == str(_date):
                self.generated_list_of_rooms = updated_list
                self.generated_list_of_dates[str(date)] = updated_list
                break
