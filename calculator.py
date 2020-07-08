import pytest
import unittest
# Here we are creating the Calculator class
class Calculator:
    # Method for adding values
    def add_values(self, num1, num2):
        return num1 + num2
    # Method for subtracting values
    def subtract_values(self, num1, num2):
        return num1 - num2
    # Method for multiplying values
    def multiply_values(self, num1, num2):
        return num1 * num2
    # Method for dividing values
    def divide_values(self, num1, num2):
        return num1 / num2

# Creating an object
simple_calc = Calculator()

print(simple_calc.add_values(5, 10))