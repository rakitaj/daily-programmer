import pytest
from algos import *
from puzzles import *


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