"""
Tests for my sorting algorithms.
"""
import pytest
import algorithms.sort as sort

@pytest.mark.parametrize("unsorted, expected", [
    ([0, 3, 3, 2, 1, 0], [0, 0, 1, 2, 3, 3]),
    ([5, -3, -2, 12, 123, 2], [-3, -2, 2, 5, 12, 123])
])
def test_bubble_sort(unsorted, expected):
    assert sort.bubble_sort(unsorted) == expected


@pytest.mark.parametrize("unsorted, expected", [
    ([0, 3, 3, 2, 1, 0], [0, 0, 1, 2, 3, 3]),
    ([5, -3, -2, 12, 123, 2], [-3, -2, 2, 5, 12, 123])
])
def test_insertion_sort(unsorted, expected):
    assert sort.insertion_sort(unsorted) == expected
