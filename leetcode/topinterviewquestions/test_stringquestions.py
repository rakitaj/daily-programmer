from leetcode.topinterviewquestions import reverse_string
import pytest


@pytest.mark.parametrize("data, expected", [(123, 321), (-123, -321), (120, 21)])
def test_reverse_string(data: int, expected: int):
    solution = reverse_string.Solution()
    actual = solution.reverse(data)
    assert actual == expected
