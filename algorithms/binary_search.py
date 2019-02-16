"""Implementation of binary search. This code related to the leetcode courses."""
from typing import List
from math import floor, sqrt

def binary_search(array: List[int], target: int) -> int:
    """Return index or -1 if target not found."""
    low = 0
    high = len(array) - 1
    while low <= high:
        middle = (high + low) // 2
        if target == array[middle]:
            return middle
        elif target < array[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return -1

def sqrt_builtin(x: int) -> int:
    return floor(sqrt(x))

def sqrt_scratch(x: int) -> int:
    low = 0
    high = x
    while guess(low, high) ** 2 != x:
        if guess(low, high) ** 2 < x:
            high = guess(low, high)
        else:
            low = guess(low, high)
    return guess(low, high)

def guess(low: int, high: int) -> int:
    return (low + high) // 2
