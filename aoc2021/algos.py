"""Common classes and algorithms for Advent of Code 2021."""
from __future__ import annotations
from typing import TypeVar, Callable, Generic


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Point):
            return self.x == __o.x and self.y == __o.y
        else:
            return False

    def __str__(self) -> str:
        return f"(x:{self.x}, y:{self.y})"

    def __repr__(self) -> str:
        return str(self)


T = TypeVar("T")


class LinqList(list[T]):
    def __init__(self, initial_list: list[T] | None = None):
        if initial_list is not None:
            self.extend(initial_list)

    def first(self) -> T:
        return self[0]

    def where(self, func: Callable[[T], bool]) -> LinqList[T]:
        results: LinqList[T] = LinqList()
        for element in self:
            if func(element) is True:
                results.append(element)
        return results

    def single(self, func: Callable[[T], bool]) -> T:
        results = self.where(func)
        if len(results) == 1:
            return results[0]
        else:
            raise Exception("More than 1 element. Single must match exactly one.")


class Grid:
    def __init__(self, numbers: list[list[int]]):
        self.x_length = len(numbers[0])
        self.y_length = len(numbers)
        self.numbers = numbers

    def get(self, x: int, y: int) -> int | None:
        # i = (self.length * y) + x
        # if x < 0 or y < 0 or i < 0 or len(self.numbers) <= i:
        #     return None
        # else:
        #     return self.numbers[i]
        if x < 0 or y < 0 or self.x_length <= x or self.y_length <= y:
            return None
        else:
            return self.numbers[y][x]

    def get_neighbors(self, x: int, y: int) -> list[int]:
        neighbors: list[int] = list()
        left = self.get(x - 1, y)
        right = self.get(x + 1, y)
        up = self.get(x, y + 1)
        down = self.get(x, y - 1)
        if left is not None:
            neighbors.append(left)
        if right is not None:
            neighbors.append(right)
        if up is not None:
            neighbors.append(up)
        if down is not None:
            neighbors.append(down)
        return neighbors


class Node(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.connections: list[Node[T]] = list()


def sliding_window(nums: list[int], start: int, lookback: int) -> int:
    total = 0
    for i in range(start - (lookback - 1), start + 1):
        total += nums[i]
    return total


def bits_to_decimal(bits: list[int], endianness: str) -> int:
    """Pass the bits least significant bit first. Aka in the 0th index."""
    total = 0
    length = len(bits)
    if endianness == "little":
        for i in range(length):
            if bits[i] == 1:
                total += pow(2, i)
    elif endianness == "big":
        # Using what looks like funky start stop because I need to hit the 0th element.
        for i in range(length - 1, -1, -1):
            if bits[i] == 1:
                total += pow(2, (length - 1) - i)
    else:
        raise ValueError(f"Endianness must be little or big. Value of {endianness} is not known.")
    return total


def most_common_bit(bits_list: list[str], i: int) -> int:
    total = 0
    for bits in bits_list:
        total += int(bits[i])
    return round(total / len(bits_list))


def count_bits(bits_list: list[str], i: int) -> tuple[int, int]:
    """Count the bits in the given position for the list of bits.
    Return a tuple in the form of (count of 0s, count of 1s)"""
    count0s = 0
    count1s = 0
    for bits in bits_list:
        if bits[i] == "0":
            count0s += 1
        elif bits[i] == "1":
            count1s += 1
        else:
            raise ValueError(f"Bit value in {bits} at position {i} is not valid.")
    return (count0s, count1s)


def diagonal_line(start: Point, end: Point) -> list[tuple[int, int]]:
    points: list[tuple[int, int]] = list()
    diagonal_length = end.x - start.x
    for i in range(diagonal_length + 1):
        point = ((start.x + i), (start.y + i))
        points.append(point)
    return points
