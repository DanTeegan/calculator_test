# Importing all from the calculator file
from calculator import *
# Importing pytest
import pytest
# Importing unit test
import unittest

# Here we are creating a new class
class Test_calc(unittest.TestCase):

    simple_calc = Calculator()
    # Running a test for the add values. Remember to use commas when testing values
    def test_add(self):
        self.assertEqual(self.simple_calc.add_values(5, 5), 10)

    # Running a test for the subtract values. Remember to use commas when testing values
    def test_subtract(self):
        self.assertEqual(self.simple_calc.subtract_values(5, 5), 0)

    # Running a test for the multiply values. Remember to use commas when testing values
    def test_multiply(self):
        self.assertEqual(self.simple_calc.multiply_values(5, 5), 25)

    # Running a test for the divide values. Remember to use commas when testing values
    def test_divide(self):
        self.assertEqual(self.simple_calc.divide_values(100, 10), 10)

