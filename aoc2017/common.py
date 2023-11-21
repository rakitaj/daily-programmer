from typing import List
"""
Common functions I will use often during Advent Of Code 2017.
"""

def number_from_text_file(path: str) -> int:
    with open(path, "r") as file:
        number_string = file.read()
        return int(number_string)

def rows_of_numbers_from_text_file(path: str) -> List[List[int]]:
    result = list()
    with open(path, "r") as file:
        lines = file.readlines()
        for line in lines:
            numbers = [int(n) for n in line.split()]
            result.append(numbers)
    return result

def lines_from_text_file(path: str) -> List[str]:
    with open(path, "r") as file:
        return file.readlines()

def numbers_from_text_file(path: str) -> List[int]:
    with open(path, "r") as file:
        string_numbers = file.read().split()
        numbers = [int(number.strip()) for number in string_numbers]
        return numbers
