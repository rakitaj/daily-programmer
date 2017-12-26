from typing import List, Callable
import common

def escape(jump_instructions: List[int], jump_modify: Callable[[int], int]) -> int:
    index = 0
    counter = 0
    while inside_bounds(jump_instructions, index):
        prev_index = index
        index += jump_instructions[index]
        counter += 1
        jump_instructions[prev_index] = jump_modify(jump_instructions[prev_index])
    return counter

def part_one(number: int) -> int:
    return number + 1

def part_two(number: int) -> int:
    if number >= 3:
        return number - 1
    else:
        return number + 1

def inside_bounds(array: int, index: int) -> bool:
    if index >= 0 and index < len(array):
        return True
    else:
        return False

if __name__ == "__main__":
    numbers = common.numbers_from_text_file("day05_input.txt")
    print(escape(numbers, part_one))
    numbers = common.numbers_from_text_file("day05_input.txt")
    print(escape(numbers, part_two))