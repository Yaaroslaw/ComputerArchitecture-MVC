from controller import *
import pickle
import jsonpickle
import yaml
import One_file_to_rule_them_all
import configparser


class View:
    def menu(self):  # Взаємодія з користувачем
        print(" 1.Show")
        print(" 2.Add day")
        print(" 3.Add month")
        print(" 4.Delete day")
        print(" 5.Delete month")
        print(" 6.Exit")
        View.choose(self)
        View.want_cont(self)

    def choose(self):
        config = configparser.RawConfigParser()
        config.read('next.ini')
        s = config.get('Section', 's')

        if s == 'pickle':
            try:
                f = open('1.txt', "rb")
                One_file_to_rule_them_all.year = pickle.load(f)
            except IOError:
                f = open('1.txt', "wb")
            f.close()

        if s == 'json':
            with open('1.json', 'r') as f:
                s2 = f.read()
                One_file_to_rule_them_all.year = jsonpickle.decode(s2)

        elif s == 'yml':
            with open('1.yml', 'r') as f:
                One_file_to_rule_them_all.year = yaml.load(f)

        n = input("Your choice: ")
        if n == "1":
            Rule.show_month(Rule())
        elif n == "2":
            Controller.add_day_param(Controller())
        elif n == "3":
            Controller.add_del_month_param(Controller(), 1)
        elif n == "4":
            Controller.del_day_param(Controller())
        elif n == "5":
            Controller.add_del_month_param(Controller(), 2)
        elif n == "6":
            exit()

        if s == 'pickle':
            f = open('1.txt', 'wb')
            pickle.dump(One_file_to_rule_them_all.year, f)

        elif s == 'json':
            with open('1.json', 'w') as f:
                str = jsonpickle.encode(One_file_to_rule_them_all.year)
                f.write(str)

        elif s == 'yml':
            with open('1.yml', 'w') as f:
                f.write(yaml.dump(One_file_to_rule_them_all.year))

    def want_cont(self):
        print("If you want to continue enter 1, else enter any key ")
        choice2 = input("Your choice: ")
        if choice2 == "1":
            View.menu(self)
        else:
            exit()

Rule.initial_values(Rule())
View.menu(View())
