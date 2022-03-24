import pytest
from leetcode.easyinterview.arrays import *


@pytest.mark.parametrize(
    "nums, k, expected",
    [([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]), ([-1, -100, 3, 99], 2, [3, 99, -1, -100])],
)
def test_rotate_array(nums: list[int], k: int, expected: list[int]):
    result = rotate_array(nums, k)
    assert result == expected


@pytest.mark.parametrize(
    "nums, k, expected",
    [([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]), ([-1, -100, 3, 99], 2, [3, 99, -1, -100])],
)
def test_rotate_array_in_place(nums: list[int], k: int, expected: list[int]):
    rotate_array_in_place(nums, k)
    assert nums == expected


@pytest.mark.parametrize("nums, expected", [([2, 2, 1], 1), ([4, 1, 2, 1, 2], 4), ([1], 1)])
def test_single_number(nums: list[int], expected: int):
    result = single_number(nums)
    assert result == expected


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1, 2, 2, 1], [2, 2], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
        ([1, 2], [1, 1], [1]),
        ([1, 1], [1, 2], [1]),
    ],
)
def test_intersection_of_two_arrays(nums1: list[int], nums2: list[int], expected: list[int]):
    result = intersection_of_two_arrays(nums1, nums2)
    assert result == expected
