import pytest
from .problem945 import Solution


@pytest.mark.parametrize("array, expected_moves, test_method", [
    ([1, 2, 2], 1, Solution().min_increment),
    ([3, 2, 1, 2, 1, 7], 6, Solution().min_increment),
    ([1, 2, 2], 1, Solution().min_increment_fast),
    ([3, 2, 1, 2, 1, 7], 6, Solution().min_increment_fast)
])
def test_min_increment(array, expected_moves, test_method):
    assert test_method(array) == expected_moves
