"""Tests for LeetCode binary search guessing game."""
import pytest
from leetcode.binarysearch.guessing import Solution

@pytest.mark.parametrize("max_number, target", [
    [10, 6],
    [1, 1]
])
def test_guessing_game(max_number: int, target: int):
    Solution.TARGET_NUMBER = target
    solution = Solution()
    assert solution.guessNumber(max_number) == target
