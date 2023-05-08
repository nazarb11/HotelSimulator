"""
# import json
#
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
#
# # convert into JSON:
# y = json.dumps(x, indent=4) # перетворює пайтон об'єкт в json формат, y присвоєно змінну типу string
#
# parse_y = json.loads(y) # перетворює строку типу джсон у об'єкт, який можна парсити (dict, list тощо)
#
# # the result is a JSON string:
# print(parse_y['name'])
#
# with open('sample.json', 'w') as wf:
#     wf.write(y)
#
#
# import json
#
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
#
# with open('sample_2.json', 'w') as sample_file:
#     json.dump(x, sample_file)
#     x = 5

# with open('sample.json', 'r') as sample_file:
#     json_obj = json.load(sample_file)
#     x = 5

# convert into JSON:
# y = json.dumps(x, indent=4) # перетворює пайтон об'єкт в json формат, y присвоєно змінну типу string
#
# parse_y = json.loads(y) # перетворює строку типу джсон у об'єкт, який можна парсити (dict, list тощо)
#
# # the result is a JSON string:
# print(parse_y['name'])
#
# with open('sample.json', 'w') as wf:
#     wf.write(y)
#
import json

with open("sample.json", "r") as tester:
    new1 = json.load(tester)

parsable_python_object = json.loads('{"name": "Parsable", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}')

parsable_python_object['name'] = 'dumped'

dumped_stre = json.dumps(parsable_python_object)
print(dumped_stre)

print(f'{new1["name"]}, {new1["age"]}')

new1["name"] = 'Roman'

with open("sample.json", "w") as tester:
    json.dump(new1, tester)

print(f'{new1["name"]}, {new1["age"]}')

# load - перетворює вміст файлу формату json у пайтон об'єкт з яким можна працювати в програмі
# dump - записуємо пайтон об'єкт у файл формату json
#
# loads - перетворює строку типу json у об'єкт, який можна парсити (dict, list тощо)
# dumps - записуємо пайтон об'єкт в json формат, повертається обєкт типу стрінг
#
"""

#1 small code to find date and time
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


#2 code to rewrite program in what date the exam will happen
exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)


#trying to save changes on laptop ...