"""Common classes and algorithms for Advent of Code 2021."""
from __future__ import annotations
from typing import Iterable, TypeVar, Callable, Generic


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        # if isinstance(other, self.__class__):
        if hasattr(other, "x") and hasattr(other, "y"):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __str__(self) -> str:
        return f"(x:{self.x}, y:{self.y})"

    def __repr__(self) -> str:
        return str(self)


T = TypeVar("T")


class LinqList(Generic[T]):
    def __init__(self, initial_list: list[T] | None = None):
        self.l: list[T] = list()
        if initial_list is not None:
            self.l.extend(initial_list)

    def __len__(self) -> int:
        return len(self.l)

    def __iter__(self):
        return self.l.__iter__()

    def __getitem__(self, i: int) -> T:
        return self.l.__getitem__(i)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, LinqList):
            return self.l == other.l
        return False

    def __repr__(self) -> str:
        return self.l.__repr__()

    def append(self, element: T) -> None:
        self.l.append(element)

    def remove(self, value: T) -> None:
        self.l.remove(value)

    def first(self) -> T:
        """Return the first element of the list."""
        return self.l[0]

    def where(self, func: Callable[[T], bool]) -> LinqList[T]:
        """Apply a filtering function to the list, returning a new list with the matching elements."""
        results: list[T] = list()
        for element in self.l:
            if func(element) is True:
                results.append(element)
        linq_list = LinqList(results)
        return linq_list

    def single(self, func: Callable[[T], bool]) -> T:
        """Return the only element of the list or throw an exception if there are none or more than one."""
        results = self.where(func)
        if len(results) == 1:
            return results.l[0]
        else:
            raise Exception("More than 1 element. Single must match exactly one.")

    def difference(self, other: Iterable[T]) -> LinqList[T]:
        """Return the elements in self that are not in other."""
        result = difference(self.l, other)
        return LinqList(result)


class Grid:
    def __init__(self, numbers: list[list[int]]):
        self.x_length = len(numbers[0])
        self.y_length = len(numbers)
        self.numbers = numbers

    def get(self, x: int, y: int) -> int | None:
        if x < 0 or y < 0 or self.x_length <= x or self.y_length <= y:
            return None
        else:
            return self.numbers[y][x]

    def set(self, x: int, y: int, value: int) -> None:
        self.numbers[y][x] = value

    def get_neighbor_values(self, x: int, y: int) -> list[int]:
        """Get the neighboring values for up, down, left, and right.
        It handles asking for out of range grid points."""
        neighbor_values: list[int | None] = [
            self.get(x - 1, y),
            self.get(x + 1, y),
            self.get(x, y + 1),
            self.get(x, y - 1),
        ]
        filtered_neighbor_values = [x for x in neighbor_values if x is not None]
        return filtered_neighbor_values

    def get_neighboring_points(self, x: int, y: int) -> list[Point]:
        """Get the neighboring points that correspond to up, down, left, and right."""
        points: list[Point] = list()
        for x_offset in range(-1, 2):
            for y_offset in range(-1, 2):
                x_target = x + x_offset
                y_target = y + y_offset
                if x_target < 0 or self.x_length <= x_target:
                    continue
                if y_target < 0 or self.y_length <= y_target:
                    continue
                if x_target == x and y_target == y:
                    continue
                points.append(Point(x_target, y_target))
        return points

    @staticmethod
    def as_zeros(x_size: int, y_size: int) -> Grid:
        result: list[list[int]] = list()
        for _ in range(y_size):
            row: list[int] = list()
            for _ in range(x_size):
                row.append(0)
            result.append(row)
        grid = Grid(result)
        return grid

    def __str__(self) -> str:
        result = "\n"
        for row in self.numbers:
            for column in row:
                result += str(column)
            result += "\n"
        return result


class GraphNode:
    def __init__(self, name: str, connections: set[tuple[str, str]] | None = None):
        self.name = name
        if connections is None:
            self.connections: set[tuple[str, str]] = set()
        else:
            self.connections = connections


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


def difference(first: list[T], second: Iterable[T]) -> list[T]:
    """Return the elements in the first list that are not in the second list."""
    diffs: list[T] = list()
    second_set: set[T] = set(second)
    for element in first:
        if element not in second_set:
            diffs.append(element)
    return diffs
