"""Implementation of binary search. This code related to the leetcode courses."""
from typing import List

def binary_search(array: List[int], target: int) -> int:
    """Return index or -1 if target not found."""
    low = 0
    high = len(array)
    while low < high:
        middle = (high + low) // 2
        if target == array[middle]:
            return middle
        elif target < array[middle]:
            high = middle
        else:
            low = middle + 1
    return -1
