import jsonpickle
from One_file_to_rule_them_all import *

class Json():
    def read(self):
        with open('2.json', 'r') as f:
            s2 = f.read()
            year = jsonpickle.decode(s2)

    def write(self):
         initial_values()
         with open('1.json', 'w') as f:
            str = jsonpickle.encode(year)
            f.write(str)