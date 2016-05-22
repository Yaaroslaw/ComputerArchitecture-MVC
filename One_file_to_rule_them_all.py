from random import randint
from model import *

year = {}


class Rule:
    # @staticmethod
    def add_day(self,pressure, temperature, wind, month, number):
        year[month].append(Day(pressure, temperature, wind, number))

    def del_day(self, month, number):
        for i in year[month]:
            if i.number == number:
                year[month].remove(i)


    def add_month(self, name):
        year[name] = []

    def del_month(self, name):
        del year[name]

    def show_month(self):  # виведення на екран інформації про місяці та дні
        for key in year:
            print(key)
        month = input("Enter the month ")
        # check
        for i in year[month]:
            # print("Number: {}, Pressure: {}, Wind: {}, Temperature: {}".format(i.number, i.pressure, i.wind, i. temperature))
            print(i)


    def initial_values(self, name):
        year[name] = []
        year[name].append(Day(1, 650, 20, 25))