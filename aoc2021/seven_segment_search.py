"""Logic to solve the seven segment search problem."""
from dataclasses import dataclass
from algos import LinqList


@dataclass
class SignalPattern:
    raw_pattern: str
    input_pattern: list[str]
    output_pattern: list[str]


def parse_signal_patterns(raw_signal_patterns: list[str]) -> list[SignalPattern]:
    result: list[SignalPattern] = list()
    for signal_pattern in raw_signal_patterns:
        parts = signal_pattern.split("|")
        input_pattern = [x.strip() for x in parts[0].split()]
        output_pattern = [x.strip() for x in parts[1].split()]
        result.append(SignalPattern(signal_pattern, input_pattern, output_pattern))
    return result


def output_pattern_counts(raw_signal_patterns: list[str]) -> int:
    counts: dict[int, int] = {}
    signal_patterns = parse_signal_patterns(raw_signal_patterns)
    for signal_pattern in signal_patterns:
        for p in signal_pattern.output_pattern:
            for i in range(8):
                if len(p) == i:
                    counts[i] = counts.get(i, 0) + 1
    return counts[2] + counts[4] + counts[3] + counts[7]


def unscramble(pattern: SignalPattern) -> dict[int, set[str]]:
    linq_list = LinqList(pattern.input_pattern)
    numbers_map: dict[int, set[str]] = dict()
    one = linq_list.single(lambda s: len(s) == 2)
    four = linq_list.single(lambda s: len(s) == 4)
    seven = linq_list.single(lambda s: len(s) == 3)
    eight = linq_list.single(lambda s: len(s) == 7)
    numbers_map[1] = set(one)
    numbers_map[4] = set(four)
    numbers_map[7] = set(seven)
    numbers_map[8] = set(eight)
    # 4 diff 9 pattern is empty.
    nine_patterns = linq_list.where(lambda s: len(s) == 6)
    nine = nine_patterns.single(lambda s: len(numbers_map[4].difference(set(s))) == 0)
    numbers_map[9] = set(nine)
    # 6 pattern diff 5 pattern is one. Must remove the 9 pattern from the 6s before doing this.
    five_patterns = linq_list.where(lambda s: len(s) == 5)
    six_patterns = linq_list.where(lambda s: len(s) == 6)
    six_patterns.remove(nine)
    for p6 in six_patterns:
        for p5 in five_patterns:
            if len(set(p6).difference(p5)) == 1:
                five = p5
                six = p6
                numbers_map[5] = set(p5)
                numbers_map[6] = set(p6)
    # 0 is the leftover 6s pattern with 6 and 9 removed.
    zero_patterns = linq_list.where(lambda s: len(s) == 6)
    zero_patterns.remove(six)
    zero_patterns.remove(nine)
    zero = zero_patterns.first()
    numbers_map[0] = set(zero)
    # 3 is either of the 5 length patterns where 9 has all
    for p5 in five_patterns:
        if len(set(p5).difference(nine)) == 0:
            three = p5
            numbers_map[3] = set(three)
    # 2 is the only one remaining.
    five_patterns.remove(three)
    five_patterns.remove(five)
    two = five_patterns.first()
    numbers_map[2] = set(two)
    return numbers_map


def unscramble_output_pattern(signal_pattern: SignalPattern) -> str:
    number_map = unscramble(signal_pattern)
    inverse_map: dict[str, int] = dict()
    for key, value in number_map.items():
        sorted_str_key = "".join(sorted(value))
        inverse_map[sorted_str_key] = key
    result = ""
    for output_pattern in signal_pattern.output_pattern:
        sorted_output_pattern = "".join(sorted(output_pattern))
        result += str(inverse_map[sorted_output_pattern])
    return result
