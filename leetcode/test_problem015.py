import pytest
import problem015 as p


@pytest.mark.parametrize("test_data, expected", [
    ([-1, 0, 1, 2, -1, -4], [(-1, -1, 2), (-1, 0, 1)])
])
def test_three_sums(test_data, expected):
    s = p.Solution()
    assert s.three_sum(test_data) == expected
