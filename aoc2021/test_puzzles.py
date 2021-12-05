"""Tests the puzzles in Advent of Code 2021 along with some test for helper function and algorithms."""
import pytest
from algos import *
from puzzles import *


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


@pytest.mark.parametrize(
    "start, lookback, expected", [(0, 1, 199), (2, 3, 607), (3, 3, 618)]
)
def test_sliding_window(start: int, lookback: int, expected: float):
    nums = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert expected == sliding_window(nums, start, lookback)


def test_sonar_sweep_simple():
    depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert sonar_sweep_lookback(depths) == 7


def test_sonar_sweep_sliding_window():
    depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert sonar_sweep_sliding_window(depths) == 5


@pytest.mark.parametrize("position, expected", [(0, 1), (1, 0), (2, 1), (3, 1), (4, 0)])
def test_most_common_bit(bits_list: list[str], position: int, expected: int):
    assert most_common_bit(bits_list, position) == expected


@pytest.mark.parametrize("bits, decimal", [([1, 0, 1, 1, 0], 22)])
def test_bits_to_decimal(bits: list[int], decimal: int):
    assert bits_to_decimal(bits, "big") == decimal


def test_calculate_oxygen_generator_rating(bits_list: list[str]):
    assert calculate_oxygen_generator_rating(bits_list) == 23


def test_calculate_co2_scrubber_rating(bits_list: list[str]):
    assert calculate_co2_scrubber_rating(bits_list) == 10
