import unittest
import fibo

class FiboTests(unittest.TestCase):

    testdata = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8)]

    def test_with_fibonacci(self):
        for data in FiboTests.testdata:
            self.assertEqual(fibo.fibonacci(data[0]), data[1])

    def test_with_fibonacci_dynamic(self):
        for data in FiboTests.testdata:
            self.assertEqual(fibo.fibonacci_dynamic(data[0]), data[1])

    def test_with_fibonacci_dynamic_func(self):
        self.calculate_with_func(fibo.fibonacci_dynamic)

    def test_with_fibonacci_func(self):
        self.calculate_with_func(fibo.fibonacci)

    def calculate_with_func(self, fibo_func):
        for data in FiboTests.testdata:
            self.assertEqual(fibo_func(data[0]), data[1])

if __name__ == "__main__":
    unittest.main()