"""Test all the code related to binary search type algorithms."""
import pytest
from .binary_search import sqrt_builtin, sqrt_scratch

@pytest.mark.parametrize("n, expected", [
    [(9, 3),
     (10, 3)]
])
def test_square_root(n: int, expected: int):
    assert sqrt_builtin(n) == expected
    assert sqrt_scratch(n) == expected
