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

@pytest.mark.parametrize("unsorted, expected", [
    ([0, 3, 3, 2, 1, 0], [0, 0, 1, 2, 3, 3]),
    ([5, -3, -2, 12, 123, 2], [-3, -2, 2, 5, 12, 123])
])
def test_selection_sort(unsorted, expected):
    assert sort.selection_sort(unsorted) == expected

@pytest.mark.parametrize("elements, start, expected", [
    ([1, 2, 3], 0, 0),
    ([1, 2, 3], 1, 1),
    ([1, 2, 3], 2, 2),
    ([8, 2, 4, 2, 6], 0, 1),
    ([8, 2, 4, 2, 6], 1, 1),
    ([8, 2, 4, 2, 6], 2, 3),
    ([8, 2, 4, 2, 6], 3, 3),
    ([8, 2, 4, 2, 6], 4, 4)
])
def test_find_minimum_element_index(elements, start, expected):
    assert sort.find_min_element_index(elements, start) == expected
