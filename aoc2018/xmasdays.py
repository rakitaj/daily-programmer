from typing import Dict, List
from xmascommon import (puzzle_input_to_ints, puzzle_input_to_strings,
                        Point, FabricClaim,
                        string_to_freq_dict, word_diff_chars, common_letters, dict_where)


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


def day03_1() -> int:
    puzzle_strings = puzzle_input_to_strings("day03.txt")
    fabric_claims: List[FabricClaim] = list()
    seen_points: Dict[Point, bool] = dict()
    for puzzle_string in puzzle_strings:
        fabric_claims.append(FabricClaim.from_puzzle_input(puzzle_string))
    for f_c in fabric_claims:
        points = f_c.points()
        for point in points:
            if point in seen_points:
                seen_points[point] = True
            else:
                seen_points[point] = False
    return len(dict_where(seen_points, lambda x: x is True))


def day03_2() -> int:
    puzzle_strings = puzzle_input_to_strings("day03.txt")
    fabric_claims: List[FabricClaim] = list()
    whole_claims = list()
    for puzzle_string in puzzle_strings:
        fabric_claims.append(FabricClaim.from_puzzle_input(puzzle_string))
    for i in range(len(fabric_claims)):
        for j in range(i, len(fabric_claims)):
            print((i, j))
            no_overlap = fabric_claims[i].overlapping_points_fast(fabric_claims[j])
            if no_overlap is True:
                whole_claims.append(fabric_claims[i])
    return whole_claims


if __name__ == "__main__":
    ANSWER = day03_2()
    print(ANSWER)
