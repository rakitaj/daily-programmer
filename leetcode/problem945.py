from typing import List


class Solution:

    def min_increment(self, array: List[int]) -> int:
        moves = 0
        for i in range(len(array)):
            while self.contains_skip_i(array, i, array[i]):
                array[i] += 1
                moves += 1
        return moves

    def min_increment_fast(self, array: List[int]) -> int:
        moves = 0
        array.sort()
        for i in range(1, len(array)):
            if array[i-1] >= array[i]:
                temp = array[i]
                array[i] = array[i-1] + 1
                moves += array[i] - temp
            print(array)
            print(moves)
        return moves

    def contains_skip_i(self, array: List[int], i_skip: int, target: int) -> bool:
        for i in range(len(array)):
            if i == i_skip:
                continue
            else:
                if array[i] == target:
                    return True
        return False

    def contains_left(self, array: List[int], position: int) -> bool:
        for i in range(position):
            if array[i] == array[position]:
                return True
        return False

    def contains_right(self, array: List[int], position: int) -> bool:
        for i in range(position, len(array)):
            if array[i] == array[position]:
                return True
        return False

    minIncrementForUnique = min_increment_fast
