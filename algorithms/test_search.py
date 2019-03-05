"""Tests for algorithms that search lists and arrays."""
import pytest
import algorithms.search as search
from leetcode.binarysearch.binary_search import binary_search

@pytest.mark.parametrize("search_data, target, expected", [
    ([5], 5, 0),
    ([5], 3, -1),
    ([1, 2, 3], 1, 0),
    ([1, 2, 3], 2, 1),
    ([1, 2, 3], 3, 2),
    ([1, 2, 3], 4, -1),
    ([1, 2, 3, 4], 2, 1),
    ([1, 2, 3, 4], 3, 2)
])
def test_binary_search(search_data, target, expected):
    assert search.binary_search(search_data, target) == expected
    reference(search_data, target, expected)
    leetcode_algo(search_data, target, expected)

def reference(search_data, target, expected):
    assert search.reference(search_data, target) == expected

def leetcode_algo(search_data, target, expected):
    assert binary_search(search_data, target) == expected
