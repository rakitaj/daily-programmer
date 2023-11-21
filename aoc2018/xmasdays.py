"""The functions for the different days of AOC 2018"""
from typing import Dict
from aoc2018.xmascommon import (
    puzzle_input_to_ints,
    puzzle_input_to_strings,
    string_to_freq_dict,
    word_diff_chars,
    common_letters,
)


def day01_1() -> int:
    """Calculate the sum of all frequency numbers."""
    numbers = puzzle_input_to_ints("day01.txt")
    return sum(numbers)


def day01_2() -> int:
    """Find the first frequency sum reached twice."""
    freq_found = False
    count = 0
    current_sum = 0
    numbers = puzzle_input_to_ints("day01.txt")
    freq_seen: Dict[int, bool] = dict()
    while freq_found is False:
        current_sum += numbers[count]
        if current_sum in freq_seen:
            break
        else:
            freq_seen[current_sum] = True
            count = (count + 1) % len(numbers)
    return current_sum


def day02_1() -> int:
    box_labels = puzzle_input_to_strings("day02.txt")
    count_2 = 0
    count_3 = 0
    for label in box_labels:
        stripped_label = label.strip()
        letter_freq = string_to_freq_dict(stripped_label)
        if any([value == 2 for key, value in letter_freq.items()]):
            count_2 += 1
        if any([value == 3 for key, value in letter_freq.items()]):
            count_3 += 1
    return count_2 * count_3


def day02_2() -> str:
    labels = puzzle_input_to_strings("day02.txt")
    for i in range(len(labels)):
        for j in range(i, len(labels)):
            if word_diff_chars(labels[i], labels[j], 1) is True:
                result = common_letters(labels[i], labels[j])
    return result.strip()


if __name__ == "__main__":
    print("Print answer here")
