# You will need to change the '?' in test_int_variable_in_string to match
# your variable in the int_variable_in_string function in the integers.py file

from unittest import TestCase
from integers import this_is_an_integer, int_variable_in_string


class Test(TestCase):
    def test_this_is_an_integer(self):
        self.assertEqual(this_is_an_integer(), type(1))

    def test_int_variable_in_string(self):
        self.assertEqual(int_variable_in_string(), "The value I assigned to my_int is: 727")