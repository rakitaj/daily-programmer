import pytest
import problem011 as p


class TestProblem(object):

    @pytest.mark.parametrize("test_data, expected", [
        ([5, 3], 3),
        ([5, 2, 5], 10),
        ([1, 2, 4, 2, 0, 4], 12),
        ([1, 2, 4, 2, 0, 4, 3], 12)
    ])
    def test_container_most_water(self, test_data, expected):
        assert p.Problem011().container_most_water(test_data) == expected

    @pytest.mark.parametrize("test_data, expected", [
        ([5, 3], 3),
        ([5, 2, 5], 10),
        ([1, 2, 4, 2, 0, 4], 12),
        ([1, 2, 4, 2, 0, 4, 3], 12),
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49)
        ])
    def test_container_most_water_linear(self, test_data, expected):
        assert p.Problem011().container_most_water_linear(test_data) == expected

    @pytest.mark.parametrize("height1, height2, distance, expected", [
        (5, 3, 3, 9),
        (5, 2, 5, 10),
        (4, 5, 3, 12),
        (9, 6, 2, 12)
    ])
    def test_calculate_area(self, height1, height2, distance, expected):
        assert p.Problem011().calculate_area(height1, height2, distance) == expected
