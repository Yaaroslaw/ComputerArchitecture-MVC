import yaml
from One_file_to_rule_them_all import *

class Yaml():
    def read(self):
         with open('2.yml', 'r') as f:
            year = yaml.load(f)


    def write(self):
        initial_values()
        with open('1.yml', 'w') as f:
            f.write(yaml.dump(year))