from One_file_to_rule_them_all import *


class Controller:
    def add_del_month_param(self,n):  # Додавання місяців
        name = input("Enter the month ")
        # check
        if n == 1:
            Rule.add_month(self, name)
        elif n == 2:
            Rule.del_month(self, name)


    def add_day_param(self):  # Додавання днів
        month = input("Enter the month ")
        # check month
        number = input("Enter the number ")
        pressure = input("Enter the pressure ")
        temperature = input("Enter the temperature ")
        wind = input("Enter the wind ")
        Rule.add_day(self,pressure, temperature, wind, month, number)


    def del_day_param(self):  # видалення днів
        month = input("Enter the month ")
        number = input("Enter the number ")
        # check
        Rule.del_day(self,month, number)
