from typing import Dict, List


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


def day01_1() -> int:
    """Calculate the sum of all frequency numbers."""
    numbers = puzzle_input_to_ints("day01.txt")
    return sum(numbers)


def day01_2() -> int:
    """Find the first frequency sum reached twice."""
    freq_found = False
    count = 0
    current_sum = 0
    numbers = puzzle_input_to_ints("day01.txt")
    freq_seen: Dict[int, bool] = dict()
    while freq_found is False:
        current_sum += numbers[count]
        if current_sum in freq_seen:
            break
        else:
            freq_seen[current_sum] = True
            count = (count + 1) % len(numbers)
    return current_sum


def string_to_freq_dict(string: str) -> Dict[str, int]:
    result: Dict[str, int] = dict()
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


def day02_1() -> int:
    box_labels = puzzle_input_to_strings("day02.txt")
    count_2 = 0
    count_3 = 0
    for label in box_labels:
        stripped_label = label.strip()
        letter_freq = string_to_freq_dict(stripped_label)
        if any([value == 2 for key, value in letter_freq.items()]):
            count_2 += 1
        if any([value == 3 for key, value in letter_freq.items()]):
            count_3 += 1
    return count_2 * count_3


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


def day02_2() -> str:
    labels = puzzle_input_to_strings("day02.txt")
    for i in range(len(labels)):
        for j in range(i, len(labels)):
            if word_diff_chars(labels[i], labels[j], 1) is True:
                result = common_letters(labels[i], labels[j])
    return result


class FabricClaim(object):    

    def __init__(self, claim_id: int, left_padding: int, top_padding: int, width: int, height: int) -> None:
        self.claim_id = claim_id
        self.left_padding = left_padding
        self.top_padding = top_padding
        self.width = width
        self.height = height

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

    def points(self):
        points: List[Point] = list()
        for x in range(self.left_padding, self.left_padding + self.width):
            for y in range(self.top_padding, self.top_padding + self.height):
                points.append(Point(x, y))
        return points


class Point(object):

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


def day03_1():
    puzzle_strings = puzzle_input_to_strings("day03.txt")
    fabric_claims: List[FabricClaim] = list()
    seen_points: List[Point] = list()
    count = 0
    for puzzle_string in puzzle_strings:
        fabric_claims.append(FabricClaim.from_puzzle_input(puzzle_string))
    for fc in fabric_claims:
        points = fc.points()
        for point in points:
            if point in seen_points:
                count += 1
            else:
                seen_points.append(point)
    return count


if __name__ == "__main__":
    answer = day03_1()
    print(answer)
