import pytest
import common



@pytest.mark.parametrize("input, expected", [
    (15, None)
])
def test_odd_number_out(input, expected):
    assert common.odd_number_out(input) == expected
