from hackerrank.common import *
import pytest

def test_true_for_all_should_be_true():
    items = [2, 4, 6, 8, 12, 16, 24]
    truth_func = lambda x: x % 2 == 0
    assert true_for_all(items, truth_func) is True

@pytest.mark.parametrize("items, func, expected_func_result, expected", [
    ([2, 4, 6, 8], lambda x: x % 2 == 0, True, True),
    ([1, 2, 4, 6, 8], lambda x: x % 2 == 0, True, False),
])
def test_check_all(items, func, expected_func_result, expected):
    assert check_all(items, func, expected_func_result) == expected

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

@pytest.mark.parametrize("numbers, expected", [
    ([0, 1, 2, 3], {0: 1, 1: 1, 2: 1, 3: 1}),
    ([0, 0, 3, 3], {0: 2, 3: 2}),
    ([0, 0, 3, 3, 7, 8, 8, 8], {0: 2, 3: 2, 7: 1, 8: 3})
])
def test_numbers_to_counts(numbers, expected):
    assert numbers_to_counts(numbers) == expected

@pytest.mark.parametrize("numbers, expected", [
    ([0, 0, 3, 3], [0, 3]),
    ([0, 0, 3, 3, 7, 8, 8, 8], [0, 3, 7, 8])
])
def test_dedupe_sequence(numbers, expected):
    assert dedupe_sequence(numbers) == expected

@pytest.mark.parametrize("number, expected", [
    (0, True),
    (1, False),
    (2, True),
    (3, False),
    (4, True)
])
def test_is_even(number, expected):
    assert is_even(number) is expected
