import pytest
import algorithms.search as search

@pytest.mark.parametrize("search_data, target, expected",[
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
    assert search.binary_search(search_data, target) == expected, f"\nTarget: {target}\nSearch data {search_data}"

def test_against_reference(search_data, target, expected):
    assert search.reference(search_data, target) == expected
