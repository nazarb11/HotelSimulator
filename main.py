import Hotel as Htl
import Receptionist as Rcp
import View as Vw
import Controller as Ctrl
from Schedule import Schedule

import datetime


def setup():
    schedule = Schedule(10, 10, 100, 200)
    rooms_list = schedule.get_generated_list_of_dates()
    receptionist_one = Rcp.Receptionist('Receptionist One', 23)
    hotel_one = Htl.Hotel('30 Euston Square', len(rooms_list[str(datetime.date.today())]), receptionist_one,
                          rooms_list, schedule)
    receptionist_one.set_hotel(hotel_one)
    vw = Vw.View(hotel_one.get_name())
    controller = Ctrl.Controller(hotel_one, receptionist_one)
    return controller, vw


if __name__ == '__main__':
    ctrl, view = setup()
    exit_opt = False
    while not exit_opt:
        view.print_greeting()
        view.print_options_list()
        choice = int(input('Choose an option: '))
        if choice == 1:
            days = int(input('Choose a number of days to stay: '))
            ctrl.choice_stay(days)

        print('\n\n')

