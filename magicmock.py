# from view import *
# from controller import *
# from model import *
from unittest import mock
from argparse import *
from One_file_to_rule_them_all import *


test = Rule()
test.add_day = mock.MagicMock()
test.add_day(0, 0, 0, 0 ,0)

test.add_month = mock.MagicMock()
test.add_month(0)

test.del_day = mock.MagicMock()
test.del_day(0,0)


# test.initial_values = mock.MagicMock()
# test.initial_values.assert_call_once_with('February')
# result = Rule.initial_values(Rule(), 'February')
# assert result == 25
# print(result)


test.del_month = mock.MagicMock()
test.del_month(0)

test.show_month = mock.MagicMock()
test.show_month()





# a = Day(0, 0, 0, 0)
#
# def f():
#     return a.number
#
# @mock.patch(a)
# def test_f(self, b):
#     b.number = 0
#     self.assertEqual(f(), 0)







