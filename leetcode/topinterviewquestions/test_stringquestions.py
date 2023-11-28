from leetcode.topinterviewquestions.stringquestions import ReverseStringSolution
import pytest


@pytest.mark.parametrize("data, expected", [(123, 321), (-123, -321), (120, 21), (1534236469, 0)])
def test_reverse_string(data: int, expected: int):
    solution = ReverseStringSolution()
    actual = solution.reverse(data)
    assert actual == expected
