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

def divide(num1, num2):
    

import unittest
class CalculatorTests(unittest.TestCase):

    def test_add1(self):
        result = add(15, 25)
        self.assertEqual(result, 40)

    def test_add2(self):
        result = add(-30, 100)
        self.assertEqual(result, 70)

    def test_multiply1(self):
        result = multiply(9, 3)
        self.assertEqual(result, 27)

    def test_multiply2(self):
        result = multiply(9, -4)
        self.assertEqual(result, -36)

    def test_multiply3(self):
        result = multiply(-4, 8)
        self.assertEqual(result, -32)

    def test_multiply4(self):
        result = multiply(-12, -9)
        self.assertEqual(result, 108)

    def test_subtract1(self):
        result = subtract(100, 30)
        self.assertEqual(result, 70)

    def test_subtract2(self):
        result = subtract(100, -30)
        self.assertEqual(result, 130)

    def test_subtract3(self):
        result = subtract(-25, 29)
        self.assertEqual(result, -54)

    def test_subtract4(self):
        result = subtract(-41, -10)
        self.assertEqual(result, -31)

if __name__ == "__main__":
    unittest.main()