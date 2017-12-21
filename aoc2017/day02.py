import common
from typing import List

def checksum(matrix: List[List[int]]) -> int:
    differences = list()
    for row in matrix:
        sorted_row = sorted(row)
        diff = sorted_row[-1] - sorted_row[0]
        differences.append(diff)
    return sum(differences)

if __name__ == "__main__":
    data = common.rows_of_numbers_from_text_file("day02_input.txt")
    print(checksum(data))
    