from typing import List

def binary_search(search_data: List[int], target: int) -> int:
    """
    Find the index of the target value in search_data. Return -1 if not found.
    """
    low = 0
    high = len(search_data) - 1
    while low <= high:
        middle = (low + high) // 2
        if target == search_data[middle]:
            return middle
        elif target > search_data[middle]:
            low = middle + 1
        else:
            high = middle - 1
    return -1

def reference(search_data, target):
    for index, element in enumerate(search_data):
        if element == target:
            return index
    return -1
