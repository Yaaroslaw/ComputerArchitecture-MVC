
from One_file_to_rule_them_all import *


def add_day_param():  # Додавання днів
    month = input("Enter the month ")
    # check month
    number = input("Enter the number ")
    pressure = input("Enter the pressure ")
    temperature = input("Enter the temperature ")
    wind = input("Enter the wind ")
    add_day(pressure, temperature, wind, month, number)


def add_del_month_param(n):  # Додавання місяців
    name = input("Enter the month ")
    # check
    if n == 1:
        add_month(name)
    elif n == 2:
        del_month(name)


def del_day_param():  # видалення днів
    month = input("Enter the month ")
    number = input("Enter the number ")
    # check
    del_day(month, number)
