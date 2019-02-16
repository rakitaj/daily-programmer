"""Test all the code related to binary search type algorithms."""
import pytest
from .binary_search import sqrt_builtin, sqrt_scratch

@pytest.mark.parametrize("sqrt_func, n, expected", [
    (sqrt_builtin, 9, 3),
    (sqrt_builtin, 8, 2),
    (sqrt_builtin, 10, 3),
    (sqrt_scratch, 9, 3),
    (sqrt_scratch, 8, 2)
])
def test_square_root(sqrt_func, n: int, expected: int):
    assert sqrt_func(n) == expected
