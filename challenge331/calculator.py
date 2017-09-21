def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    total = num1
    if num2 > 0:
        for i in range(num2):
            total = add(total, -1)
    else:
        for i in range(0, num2, -1):
            total = add(total, 1)
    return total

def multiply(num1, num2):
    total = 0
    if num2 > 0:
        for i in range(num2):
            total = add(total, num1)
    else:
        for i in range(0, num2, -1):
            total = subtract(total, num1)
    return total

def absolute_value(num):
    if num < 0:
        return multiply(num, -1)
    else:
        return num

def calculate_sign(num1, num2):
    sign = 0
    if num1 > 0 and num2 > 0:
        sign = 1
    elif num1 < 0 and num2 < 0:
        sign = 1
    else:
        sign = -1
    return sign

def divide(num1, num2):
    sign = calculate_sign(num1, num2)
    num1 = absolute_value(num1)
    num2 = absolute_value(num2)
    if num2 == 0:
        return "Not-defined"
    else:
        count = 0
        while num1 > 0:
            num1 = subtract(num1, num2)
            count = add(count, 1)
        if num1 == 0:
            return count * sign
        else:
            return "Non-integral answer"

import unittest
class CalculatorTests(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(15, 25), 40)
        self.assertEqual(add(-30, 100), 70)

    def test_multiply(self):
        self.assertEqual(multiply(9, 3), 27)
        self.assertEqual(multiply(9, -4), -36)
        self.assertEqual(multiply(-4, 8), -32)
        self.assertEqual(multiply(-12, -9), 108)

    def test_abosulute_value(self):
        self.assertEqual(absolute_value(3), 3)
        self.assertEqual(absolute_value(-3), 3)

    def test_subtract(self):
        self.assertEqual(subtract(100, 30), 70)
        self.assertEqual(subtract(100, -30), 130)
        self.assertEqual(subtract(-25, 29), -54)
        self.assertEqual(subtract(-41, -10), -31)

    def test_divide(self):
        self.assertEqual(divide(100, 2), 50)
        self.assertEqual(divide(0, 0), "Not-defined")
        self.assertEqual(divide(75, -3), -25)
        self.assertEqual(divide(-75, 3), -25)
        self.assertEqual(divide(7, 3), "Non-integral answer")

if __name__ == "__main__":
    unittest.main()