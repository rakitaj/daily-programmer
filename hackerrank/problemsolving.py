from typing import Sequence, List, Tuple
import re
import itertools
import sys


def simple_sum_array(count: int, numbers: Sequence[int]) -> int:
    return sum(numbers)


def compare_the_triplets(alice: Tuple[int, int, int], bob: Tuple[int, int, int]) -> Tuple[int, int]:
    alice_score = 0
    bob_score = 0
    for index, _ in enumerate(alice):
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
    return (positive_count / size, negative_count / size, zero_count / size)


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
        for r in permute(data[:i] + data[i + 1 :]):
            res.append([c] + r)
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
