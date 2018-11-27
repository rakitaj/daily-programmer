import pytest
import leetcode.problem009 as p


@pytest.mark.parametrize("test_data, expected", [
    (121, True),
    (-121, False),
    (10, False)
])
def test_is_palindrome(test_data: int, expected: bool):
    assert p.Solution().is_palindrome(test_data) == expected
