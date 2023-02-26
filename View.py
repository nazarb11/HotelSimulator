import json


class View:
    def __init__(self, greeting_message=None):
        self.greeting_message = greeting_message if greeting_message else 'Hotel Program'
        self.choice = None
        self.options_list = None
        with open('options_list.json', 'r') as options_json:
            self.options_list = json.load(options_json)

    def print_greeting(self):
        print(self.greeting_message + '\n\n')

    def print_options_list(self):
        print('Select what you want to do:')
        keys = self.options_list.keys()
        counter = 1
        for key in keys:
            print(f'Option {counter}: {key}')
            counter = counter + 1
        print('\n\n')

