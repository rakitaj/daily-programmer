import pytest
from problem011 import *

class TestProblem(object):

    @pytest.mark.parametrize("test_data, expected", [
        ([5, 3], 3),
        ([5, 2, 5], 10),
        ([1, 2, 4, 2, 0, 4], 12),
        ([1, 2, 4, 2, 0, 4, 3], 12)
    ])
    def test_container_most_water(self, test_data, expected):
        assert container_most_water(test_data) == expected

    @pytest.mark.parametrize("height1, height2, distance, expected", [
        (5, 3, 3, 9),
        (5, 2, 5, 10),
        (4, 5, 3, 12),
        (9, 6, 2, 12)
    ])
    def test_calculate_area(self, height1, height2, distance, expected):
        assert calculate_area(height1, height2, distance) == expected
