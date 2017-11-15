from typing import Tuple, Dict
import unittest

def first_repeating_character(characters: str) -> Tuple[int, str]:
    chars: Dict[str, int] = {}
    for index, char in enumerate(characters):
        if char in chars:
            return (index, char)
        else:
            chars[char] = 1
    return (None, None)


class RepeatingCharacterTests(unittest.TestCase):
    """Tests for the repeating chacter function based on DailyProgrammer examples."""

    def test_sample_input(self):
        result = first_repeating_character("ABCDEBC")
        self.assert_helper(result, 5, "B")

    def test_challenge_input_1(self):
        result = first_repeating_character("IKEUNFUVFV")
        self.assert_helper(result, 6, "U")

    def test_challenge_input_2(self):
        result = first_repeating_character("PXLJOUDJVZGQHLBHGXIW")
        self.assert_helper(result, 7, "J")

    def test_challenge_input_3(self):
        result = first_repeating_character("*l1J?)yn%R[}9~1\"=k7]9;0[$")
        self.assert_helper(result, 14, "1")

    def assert_helper(self, result, expected_index, expected_char):
        self.assertEqual(result[0], expected_index)
        self.assertEqual(result[1], expected_char)

if __name__ == "__main__":
    unittest.main()
