from typing import List


def min_increment(array: List[int]) -> int:
    moves = 0
    for i in range(len(array)):
        while contains_skip_i(array, i, array[i]):
            array[i] += 1
            moves += 1
    return moves


def contains_skip_i(array: List[int], i_skip: int, target: int) -> bool:
    for i in range(len(array)):
        if i == i_skip:
            continue
        else:
            if array[i] == target:
                return True
    return False

