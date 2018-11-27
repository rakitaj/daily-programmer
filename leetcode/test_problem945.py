import pytest
from .problem945 import min_increment


@pytest.mark.parametrize("array, expected_moves", [
    ([1, 2, 2], 1),
    ([3, 2, 1, 2, 1, 7], 6)
])
def test_min_increment(array, expected_moves):
    assert min_increment(array) == expected_moves
