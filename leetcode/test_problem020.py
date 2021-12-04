"""Tests Leetcode problem 20"""
import pytest
from leetcode.problem020 import Solution


@pytest.mark.parametrize(
    "test_input, expected_result",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("]", False),
    ],
)
def test_valid_parenthesis(test_input: str, expected_result: bool):
    solution = Solution()
    print(test_input)
    print(expected_result)
    assert solution.isValid(test_input) == expected_result
