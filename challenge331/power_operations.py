import unittest

class PowerOperations:

    @staticmethod
    def sum_digits(number):
        sum = 0
        for char in str(number):
            sum = sum + int(char)
        return sum

    @staticmethod
    def sum_digits_exponent(base, power):
        number = pow(base, power)
        return PowerOperations.sum_digits(number)

class PowerOperationsTests(unittest.TestCase):

    def test_sum_digits(self):
        self.simple_assert_harness(1, 1)
        self.simple_assert_harness(123, 6)
        self.simple_assert_harness(101, 2)

    def test_sum_exponent(self):
        self.exponent_sum_assert_harness(4, 2, 7)
        self.exponent_sum_assert_harness(10, 10, 1)

    def simple_assert_harness(self, number, expected_total):
        actual_total = PowerOperations.sum_digits(number)
        self.assertEqual(expected_total, actual_total)

    def exponent_sum_assert_harness(self, base, exponent, expected_total):
        actual_total = PowerOperations.sum_digits_exponent(base, exponent)
        self.assertEqual(expected_total, actual_total)

if __name__ == "__main__":
    unittest.main()