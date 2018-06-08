from typing import List

def true_for_all(items: List, func) -> bool:
    for item in items:
        result = func(item)
        if result is not True:
            return False
    return True

def sum_desired_length(numbers: List[int], start: int, length: int) -> int:
    total = 0
    for i in range(start, start + length):
        total += numbers[i]
    return total

def check_all(items: List, func, expected_func_result) -> bool:
    for item in items:
        result = func(item)
        if result != expected_func_result:
            return False
    return True