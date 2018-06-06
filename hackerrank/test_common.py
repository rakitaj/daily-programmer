from common import true_for_all, sum_desired_length
import pytest

def test_true_for_all_should_be_true():
    items = [2, 4, 6, 8, 12, 16, 24]
    truth_func = lambda x: x % 2 == 0
    assert true_for_all(items, truth_func) is True

def test_true_for_all_with_bad_data_should_be_false():
    items = [2, 4, 6, 8, 13, 16, 24]
    truth_func = lambda x: x % 2 == 0
    assert true_for_all(items, truth_func) is False

@pytest.mark.parametrize("numbers, start, length, expected", [
    ([1, 2, 3], 0, 3, 6),
    ([1, 2, 3], 1, 2, 5),
    ([1, 2, 3, 4, 5], 1, 4, 14)
])
def test_sum_desired_length(numbers, start, length, expected):
    assert sum_desired_length(numbers, start, length) == expected
