# from view import *
# from controller import *
# from model import *
from unittest import mock
from argparse import *
from One_file_to_rule_them_all import *
from controller import *
from view import *


test = Rule()
test.add_day = mock.MagicMock()
test.add_day(0, 0, 0, 0, 0)

test.add_month = mock.MagicMock()
test.add_month(0)

test.del_day = mock.MagicMock()
test.del_day(0,0)

test.del_month = mock.MagicMock()
test.del_month(0)

test.show_month = mock.MagicMock()
test.show_month()

test = Controller
test.add_del_month_param = mock.MagicMock()
test.add_del_month_param(Controller, 0)

test.add_day_param = mock.MagicMock()
test.add_day_param(Controller)

test.del_day_param = mock.MagicMock()
test.del_day_param(Controller)

test = View
test.choose = mock.MagicMock()
test.choose(View)

test.want_cont = mock.MagicMock()
test.want_cont(View)




# a = Day(0, 0, 0, 0)
#
# def f():
#     return a.number
#
# @mock.patch(a)
# def test_f(self, b):
#     b.number = 0
#     self.assertEqual(f(), 0)







