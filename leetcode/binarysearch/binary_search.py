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

def close_enough(guess: float, target: int, delta: float) -> bool:
    diff = target - guess
    return abs(diff) <= delta

def sqrt_scratch(x: int) -> int:
    if x == 1:
        return 1
    low = 0
    high = x
    guess = (low + high) / 2
    while close_enough(guess ** 2, x, .01) is False:
        if guess ** 2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
    return floor(guess)
