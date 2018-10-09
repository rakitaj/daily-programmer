"""
Code to solve the circular array rotation problem on Hacker Rank.
"""
from typing import List, Tuple
import pytest

def circular_array_rotation(array: List[int], shifts: int, queries: List[int]) -> List[int]:
    results: List[int] = list()
    for index in queries:
        adjusted_index = (index + shifts - 1) % len(array)
        result = array[adjusted_index]
        results.append(result)
    return results

def read_test_input(path: str) -> Tuple[List[int], int, List[int]]:
    queries: List[int] = list()
    with open(path, "r") as f:
        lines = f.readlines()
    for index, line in enumerate(lines):
        if index == 0:
            string_numbers = line.split()
            array_length = int((string_numbers[0]))
            shift = int(string_numbers[1])
            query_length = int(string_numbers[2])
        elif index == 1:
            array = [int(number) for number in line.split()]
        else:
            queries.append(int(line))
    return (array, shift, queries)

def read_test_output(path: str) -> List[int]:
    with open(path, "r") as f:
        lines = f.readlines()
    expected = [int(number) for number in lines.split()]
    return expected    

@pytest.mark.parametrize("array, shifts, queries, expected", [
    ([1, 2, 3], 2, [0, 1, 2], [2, 3, 1]),
    ([1, 2, 3, 4, 5], 8, [0, 1, 2, 3, 4], [3, 4, 5, 1, 2]),
    ([23], 0, [0], [23])
])
def test_circular_array_rotation(self, array, shifts, queries, expected):
    assert circular_array_rotation(array, shifts, queries) == expected

#def test_circular_array_rotaion_