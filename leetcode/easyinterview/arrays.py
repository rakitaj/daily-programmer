import enum


def rotate_array(nums: list[int], k: int) -> list[int]:
    rotated_array = list(nums)
    for i, _ in enumerate(nums):
        ii = (i + k) % len(nums)
        rotated_array[ii] = nums[i]
    return rotated_array


def rotate_array_in_place(nums: list[int], k: int) -> None:
    rotated_array = rotate_array(nums, k)
    for i, _ in enumerate(nums):
        nums[i] = rotated_array[i]


def single_number(nums: list[int]) -> int:
    result = 0
    for n in nums:
        result = result ^ n
    return result


def intersection_of_two_arrays(nums1: list[int], nums2: list[int]) -> list[int]:
    result: list[int] = list()
    number_dict: dict[int, int] = dict()
    if len(nums1) < len(nums2):
        for n in nums2:
            number_dict.setdefault(n, 0)
            number_dict[n] += 1
        for n in nums1:
            if n in number_dict and 0 < number_dict[n]:
                result.append(n)
                number_dict[n] -= 1
    else:
        for n in nums1:
            number_dict.setdefault(n, 0)
            number_dict[n] += 1
        for n in nums2:
            if n in number_dict and 0 < number_dict[n]:
                result.append(n)
                number_dict[n] -= 1
    return result
