from typing import Sequence, List, Tuple
import re
import itertools
import sys
import time

def simple_sum_array(count: int, numbers: Sequence[int]) -> int:
    return sum(numbers)

def compare_the_triplets(alice: Tuple[int, int, int], bob: Tuple[int, int, int]) -> Tuple[int, int]:
    alice_score = 0
    bob_score = 0
    for index, element in enumerate(alice):
        if alice[index] > bob[index]:
            alice_score += 1
        elif bob[index] > alice[index]:
            bob_score += 1
        else:
            pass
    return (alice_score, bob_score)

def diagonal_difference(matrix: List[List[int]]) -> int:
    diagonal_forward = 0
    diagonal_backward = 0
    for i in range(0, len(matrix)):
        diagonal_forward += matrix[i][i]
        j = len(matrix) - 1 - i
        diagonal_backward += matrix[j][i]
    return abs(diagonal_forward - diagonal_backward)

def plus_minus(numbers: List[int]) -> Tuple[float, float, float]:
    size = len(numbers)
    positive_count = 0
    negative_count = 0
    zero_count = 0
    for n in numbers:
        if n > 0:
            positive_count += 1
        elif n < 0:
            negative_count += 1
        else:
            zero_count += 1
    return (positive_count/size, negative_count/size, zero_count/size)

def staircase(count: int) -> str:
    result = ""
    for i in range(1, count + 1):
        spaces = " " * (count - i)
        hashes = "#" * i
        result += f"{spaces}{hashes}\n"
    return result

def mini_max_sum(numbers: List[int]) -> Tuple[int, int]:
    combinations = itertools.combinations(numbers, 4)
    max_sum = 0
    min_sum = sys.maxsize
    for combination in combinations:
        total = sum(combination)
        if total > max_sum:
            max_sum = total
        if total < min_sum:
            min_sum = total
    return (min_sum, max_sum)

def permute(data):
    if len(data) <= 1:
        return [data]
    res = []
    for i, c in enumerate(data):
        for r in permute(data[:i]+data[i+1:]):
            res.append([c]+r)
    return res

def birthday_cake_candles(candle_heights: List[int]) -> int:
    max_height = max(candle_heights)
    candles_of_that_height = filter(lambda x: x == max_height, candle_heights)
    return len(list(candles_of_that_height))

def time_conversion(time_12h: str) -> str:
    pattern_am_12 = re.compile("12:..:..AM")
    pattern_pm_12 = re.compile("12:..:..PM")
    pattern_am = re.compile("..:..:..AM")
    pattern_pm = re.compile("..:..:..PM")
    if pattern_am_12.match(time_12h):
        return "00" + time_12h[2:-2]
    elif pattern_am.match(time_12h) or pattern_pm_12.match(time_12h):
        return time_12h[:-2]
    else:
        hours = int(time_12h.split(":")[0])
        hours = (hours + 12) % 24
        return str(hours) + time_12h[2:-2]

class TestProblemSolving(object):
    
    def test_simple_sum_array(self):
        assert simple_sum_array(6, [1, 2, 3, 4, 10, 11]) == 31

    def test_compare_the_triplets(self):
        assert compare_the_triplets((5, 6, 7), (3, 6, 10)) == (1, 1)

    def test_diagonal_difference(self):
        test_data = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
        assert diagonal_difference(test_data) == 15

    def test_plus_minus(self):
        test_data = [-4, 3, -9, 0, 4, 1]
        result = plus_minus(test_data)
        assert round(result[0], 6) == 0.500000
        assert round(result[1], 6) == 0.333333
        assert round(result[2], 6) == 0.166667

    def test_staircase(self):
        expected = "     #\n    ##\n   ###\n  ####\n #####\n######\n"
        assert staircase(6) == expected

    def test_mini_max_sum(self):
        assert mini_max_sum([1, 2, 3, 4, 5]) == (10, 14)

    def test_birthday_cake_candles(self):
        assert birthday_cake_candles([3, 2, 1, 3]) == 2

    def test_time_conversion(self):
        assert time_conversion("12:00:00AM") == "00:00:00"
        assert time_conversion("12:01:01AM") == "00:01:01"
        assert time_conversion("12:35:00AM") == "00:35:00"
        assert time_conversion("01:23:45AM") == "01:23:45"
        assert time_conversion("12:00:00PM") == "12:00:00"
        assert time_conversion("12:30:00PM") == "12:30:00"
        assert time_conversion("07:05:45AM") == "07:05:45"
        assert time_conversion("07:05:45PM") == "19:05:45"

        for half in ["AM", "PM"]:
            for hour in range(1, 13):
                for minute in range(1, 60):
                    for second in range(1, 60):
                        stime = str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(second).zfill(2) + half
                        result = time_conversion(stime)
                        time_tuple = time.strptime(stime, "%I:%M:%S%p")
                        expected = time.strftime("%H:%M:%S", time_tuple)
                        assert result == expected, f"Raw: {stime} Expected: {expected} Actual:{result}"
