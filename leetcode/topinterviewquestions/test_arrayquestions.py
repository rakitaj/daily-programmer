from leetcode.topinterviewquestions.arrayquestions import (
    ContainsDuplicate,
    ArrayPlusOne,
    MoveZeros,
    RemoveDuplicates,
)
import pytest


@pytest.mark.parametrize("nums, expected", [([1, 2, 3, 1], True), ([1, 2, 3, 4], False)])
def test_array_contains_duplicate(nums: list[int], expected: bool):
    solver = ContainsDuplicate()
    actual = solver.containsDuplicate(nums)
    assert actual == expected


@pytest.mark.parametrize(
    "digits, expected",
    [([1, 2, 3], [1, 2, 4]), ([4, 3, 2, 1], [4, 3, 2, 2]), ([9], [1, 0]), ([1, 9, 9], [2, 0, 0])],
)
def test_array_plus_one(digits: list[int], expected: list[int]):
    solver = ArrayPlusOne()
    actual = solver.plusOne(digits)
    assert actual == expected


@pytest.mark.parametrize(
    "nums, expected", [([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]), ([0], [0]), ([0, 0, 1], [1, 0, 0])]
)
def test_move_zeroes(nums: list[int], expected: list[int]):
    solver = MoveZeros()
    solver.move_zeroes_v2(nums)
    assert nums == expected


@pytest.mark.parametrize(
    "nums, expected, k",
    [([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4, -1, -1, -1, -1, -1], 5), ([1, 1, 2], [1, 2, -1], 2)],
)
def test_remove_duplicates(nums: list[int], expected: list[int], k: int):
    solver = RemoveDuplicates()
    count = solver.remove_dupes(nums)
    assert count == k
    for i in range(k):
        assert nums[i] == expected[i]
