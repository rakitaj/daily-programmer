import pytest
from algos import *


@pytest.fixture
def bits_list() -> list[str]:
    return [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]


@pytest.mark.parametrize("start, lookback, expected", [(0, 1, 199), (2, 3, 607), (3, 3, 618)])
def test_sliding_window(start: int, lookback: int, expected: float):
    nums = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert expected == sliding_window(nums, start, lookback)


@pytest.mark.parametrize("position, expected", [(0, 1), (1, 0), (2, 1), (3, 1), (4, 0)])
def test_most_common_bit(bits_list: list[str], position: int, expected: int):
    assert most_common_bit(bits_list, position) == expected


@pytest.mark.parametrize("bits, decimal", [([1, 0, 1, 1, 0], 22)])
def test_bits_to_decimal(bits: list[int], decimal: int):
    assert bits_to_decimal(bits, "big") == decimal


@pytest.mark.parametrize("start, end, expected", [((0, 0), (0, 0), True), ((0, 5), (5, 0), False)])
def test_point(start: tuple[int, int], end: tuple[int, int], expected: bool):
    point1 = Point(start[0], start[1])
    point2 = Point(end[0], end[1])
    assert (point1 == point2) is expected
