import pickle
from One_file_to_rule_them_all import *

class Pickle():
    def read(self):
        try:
            f = open('2.txt', "rb")
            year = pickle.load(f)
        except IOError:
            f = open('1.txt', "wb")
        f.close()

    def write(self):
        initial_values()
        f = open('1.txt', 'wb')
        pickle.dump(year, f)