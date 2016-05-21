import unittest
from pckl import *
from ymll import *
from jjson import *
from io import StringIO
from One_file_to_rule_them_all import *


class TestPickle(unittest.TestCase):
    def test(self):
        initial_values()
        Pickle.write(self)
        str = "Ђ}q (X   Februaryq]q(cmodelDayq)Ѓq}q(X   pressureqMX   numberqKX   windqKX   temperatureq	Kubh)Ѓq}q(hM)hKhKh	K ubh)Ѓq}q(hM%hKhKh	Jыяяяubh)Ѓq}q(hMЇhKhKh	JыяяяubeX   Marchq]qu."
        outp = StringIO()
        with open('2.txt', 'rb') as f:
            outp.write(f.read)
        self.assertEqual(outp.getvalue(), str)



class TestJson(unittest.TestCase):
    def test(self):
        Json.write(self)
        str = "{'June': [{'temperature': '1', 'wind': '1', 'pressure': '1', 'py/object': 'model.Day', 'number': '1'}]}"
        outp = StringIO()
        with open('2.json', 'r') as f:
            outp.write(f.read())
        self.assertEqual(outp.getvalue(), str)


class TestYaml(unittest.TestCase):
    def test(self):
        Yaml.write(self)
        str = "July:\n- !!python/object:model.Day {number: '2', pressure: '20', temperature: '20', wind: '20'}"
        outp = StringIO()
        with open('2.yml', 'rt') as f:
            outp.write(f.read())
        self.assertEqual(outp.getvalue(), str)

if __name__ == '__main__':
    unittest.main()