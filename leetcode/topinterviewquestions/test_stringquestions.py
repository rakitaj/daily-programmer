from leetcode.topinterviewquestions import reverse_string
import pytest


def test_reverse_string():
    solution = reverse_string.Solution()
    actual = solution.reverse(123)
    assert actual == 321
