"""LeetCode 8. String to Integer (atoi)"""
import re

def a_to_i(string: str) -> int:
    stripped_string = string.strip()
    result = re.match(r"([+-]?\d+)", stripped_string)
    if result is None:
        return 0
    else:
        # INT_MAX (2^31 − 1) or INT_MIN (−2^31)
        # Bounds check for sake of the problem
        number = int(result.group(0))
        if number > (2 ** 31 - 1):
            return 2147483647
        elif number < (-2 ** 31):
            return -2147483648
        else:
            return number
