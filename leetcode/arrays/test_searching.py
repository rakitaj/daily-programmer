from searching import *
import pytest


@pytest.mark.parametrize("numbers, expected", [([10, 2, 5, 3], True), ([7, 1, 14, 11], True)])
def test_n_and_double_present(numbers: list[int], expected: bool):
    actual = check_if_n_and_double_exists(numbers)
    assert actual is expected


@pytest.mark.parametrize(
    "arr, expected",
    [([2, 1], False), ([3, 5, 5], False), ([0, 3, 2, 1], True), ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], False), ([9,8,7,6,5,4,3,2,1,0], False)],
)
def test_is_valid_mountain_array(arr: list[int], expected: bool):
    actual = valid_mountain_array(arr)
    assert actual is expected
