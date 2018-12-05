from typing import List


def puzzle_input_to_ints(filename: str) -> List[int]:
    result: List[int] = list()
    with open(f"./puzzle-input/{filename}") as f:
        for line_of_text in f:
            result.append(int(line_of_text))
    return result


def day_01() -> int:
    """Calculate the sum of all frequency numbers"""
    puzzle_data = puzzle_input_to_ints("day01.txt")
    return sum(puzzle_data)


if __name__ == "__main__":
    print(day_01())