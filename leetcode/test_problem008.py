"""Tests for LeetCode 8. String to Integer (atoi)"""
import pytest
from leetcode.problem008 import a_to_i

@pytest.mark.parametrize("string, expected_number", [
    ["42", 42],
    ["   -42", -42],
    ["4193 with words", 4193],
    ["words and 987", 0],
    ["+1", 1]
])
def test_a_to_i(string, expected_number):
    assert a_to_i(string) == expected_number
