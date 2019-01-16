"""
Advent of Code 2018 solutions.
"""
from typing import Dict, List, Callable


def puzzle_input_base(filename: str, cast_func) -> List:
    result: List = list()
    with open(f"puzzle-input/{filename}", "r") as f:
        for line in f:
            result.append(cast_func(line))
    return result


def puzzle_input_to_ints(filename: str) -> List[int]:
    return puzzle_input_base(filename, int)


def puzzle_input_to_strings(filename: str) -> List[str]:
    return puzzle_input_base(filename, str)


def dict_where(dictionary: Dict, where_func: Callable) -> Dict:
    result = dict()
    for key, value in dictionary.items():
        if where_func(value) is True:
            result[key] = value
    return result


def string_to_freq_dict(string: str) -> Dict[str, int]:
    result: Dict[str, int] = dict()
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


def common_letters(word_1: str, word_2: str) -> str:
    if len(word_1) != len(word_2):
        raise ValueError("Words must be the same length for common letter comparison.")
    result = ""
    for i in range(len(word_1)):
        if word_1[i] == word_2[i]:
            result += word_1[i]
    return result


def word_diff_chars(word_1: str, word_2: str, target_diff: int) -> bool:
    count = 0
    for i in range(len(word_1)):
        if word_1[i] != word_2[i]:
            count += 1
    return count == target_diff


class Point(object):

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

class ClaimedPoint(Point):

    def __init__(self, x: int, y: int, claim_id: int) -> None:
        super().__init__(x, y)
        self.claim_id = claim_id

    def __eq__(self, other) -> bool:
        return super().__eq__(other) and self.claim_id == other.claim_id

    def __repr__(self) -> str:
        return f"ID:{self.claim_id} - ({self.x}, {self.y})"

    def __hash__(self):
        return hash((self.x, self.y, self.claim_id))


class FabricClaim(object):
    """A claim on an area of fabric."""

    def __init__(self, claim_id: int, left_padding: int, top_padding: int, width: int, height: int) -> None:
        self.claim_id = claim_id
        self.left_padding = left_padding
        self.top_padding = top_padding
        self.width = width
        self.height = height
        self.area = self.width = self.height

    @staticmethod
    def from_puzzle_input(claim_string: str) -> "FabricClaim":
        """Claim format: #123 @ 3,2: 5x4"""
        claim_parts = claim_string.split("@")
        claim_id = int(claim_parts[0].strip().strip("#"))
        size_parts = claim_parts[1].split(":")
        paddings = size_parts[0].split(",")
        left_padding = int(paddings[0].strip())
        top_padding = int(paddings[1].strip())
        sizes = size_parts[1].split("x")
        width = int(sizes[0].strip())
        height = int(sizes[1].strip())
        return FabricClaim(claim_id, left_padding, top_padding, width, height)

    def points(self) -> Dict[Point, bool]:
        points: Dict["Point", bool] = dict()
        for x in range(self.left_padding, self.left_padding + self.width):
            for y in range(self.top_padding, self.top_padding + self.height):
                points[Point(x, y)] = False
        return points

    def overlapping_points(self, other: "FabricClaim") -> List[Point]:
        overlapping_points: List[Point] = list()
        points = self.points()
        other_points = other.points()
        for other_point in other_points:
            if other_point in points:
                overlapping_points.append(other_point)
        return overlapping_points

    def overlapping_points_fast(self, other: "FabricClaim") -> bool:
        points = self.points()
        other_points = other.points()
        for other_point in other_points:
            if other_point in points:
                return False
        return True
