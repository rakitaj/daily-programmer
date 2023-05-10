from typing import TypeVar, Callable, Sequence

T = TypeVar("T")
R = TypeVar("R")


def true_for_all(items: list[T], func: Callable[[T], bool]) -> bool:
    for item in items:
        result = func(item)
        if result is not True:
            return False
    return True


def sum_desired_length(numbers: list[int], start: int, length: int) -> int:
    total = 0
    for i in range(start, start + length):
        total += numbers[i]
    return total


def check_all(items: list[T], func: Callable[[T], R], expected_func_result: R) -> bool:
    for item in items:
        result = func(item)
        if result != expected_func_result:
            return False
    return True


def numbers_to_counts(numbers: Sequence[int]) -> dict[int, int]:
    counts: dict[int, int] = dict()
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    return counts


def dedupe_sequence(sequence: Sequence[T]) -> list[T]:
    uniques: list[T] = list()
    for element in sequence:
        if element not in uniques:
            uniques.append(element)
    return uniques


def is_even(number: int) -> bool:
    return number % 2 == 0
