from typing import List
import os
import unittest

class Minefield(object):

    def __init__(self, minefield_grid: List[List[str]]) -> None:
        self.minefield = minefield_grid

def create_minefield(user_input: str) -> List[List[str]]:
    minefield = list()
    rows = user_input.split("\n")
    rows = [r.strip() for r in rows if len(r.strip()) > 0]
    for row in rows:
        chars = list()
        for char in row:
            chars.append(char)
        minefield.append(chars)
    return minefield

class MinefieldTests(unittest.TestCase):

    def test_creation_from_hardcoded_input(self):
        sample_input = """
        ++++
        +*0+
        M00+
        ++++
        """
        expected = [["+", "+", "+", "+"], ["+", "*", "0", "+"], ["M", "0", "0", "+"], ["+", "+", "+", "+"]]
        actual = create_minefield(sample_input)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()