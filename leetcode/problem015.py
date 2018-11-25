from typing import List, Tuple, Set


def three_sum(numbers: List[int]) -> List[Tuple[int, int, int]]:
    length = len(numbers)
    zero_sums: Set[Tuple[int, int, int]] = set()
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if numbers[i] + numbers[j] + numbers[k] == 0:
                    sorted_sum_iterable = sorted([numbers[i], numbers[j], numbers[k]])
                    first, second, third = tuple(sorted_sum_iterable)
                    zero_sums.add((first, second, third))
    return list(zero_sums)
