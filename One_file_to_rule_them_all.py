from random import randint
from model import *

year = {}


def add_day(pressure, temperature, wind, month, number):
    year[month].append(Day(pressure, temperature, wind, number))


def del_day(month, number):
    for i in year[month]:
        if i.number == number:
            year[month].remove(i)


def add_month(name):
    year[name] = []


def del_month(name):
    del year[name]


def show_month():  # виведення на екран інформації про місяці та дні
    for key in year:
        print(key)
    month = input("Enter the month ")
    # check
    for i in year[month]:
        print("Number: {}, Pressure: {}, Wind: {}, Temperature: {}".format(i.number, i.pressure, i.wind, i. temperature))


def initial_values():
    year["February"] = []
    for i in range(25, 29):
        x = randint(684, 809)
        y = randint(-9, 10)
        z = randint(1, 30)
        year["February"].append(Day(x, y, z, i))