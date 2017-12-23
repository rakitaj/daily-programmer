import common
from typing import List

def checksum(matrix: List[List[int]], checksum_function) -> int:
    all_checksums = list()
    for row in matrix:
        diff = checksum_function(row)
        all_checksums.append(diff)
    return sum(all_checksums)

def diff_checksum(row: List[int]) -> int:
    sorted_row = sorted(row)
    diff = sorted_row[-1] - sorted_row[0]
    return diff

def div_checksum(row: List[int]) -> int:
    for i in range(len(row)):
        for j in range(i + 1, len(row)):
            higher = max(row[i], row[j])
            lower = min(row[i], row[j])
            if higher % lower == 0:
                return int(higher / lower)

if __name__ == "__main__":
    data = common.rows_of_numbers_from_text_file("day02_input.txt")
    print(checksum(data, diff_checksum))
    print(checksum(data, div_checksum))
