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
    # Remove numbers that are figured out.
    linq_list.remove(one)
    linq_list.remove(four)
    linq_list.remove(seven)
    linq_list.remove(eight)
    # Figure out three
    five_patterns = linq_list.where(lambda s: len(s) == 5)
    assert len(five_patterns) == 3
    for p5 in five_patterns:
        if len(numbers_map[1].intersection(p5)) == 2:
            three = p5
            numbers_map[3] = set(three)
            linq_list.remove(three)
            break
    # Figure out five
    five_patterns = linq_list.where(lambda s: len(s) == 5)
    assert len(five_patterns) == 2
    for p5 in five_patterns:
        if len(numbers_map[4].difference(one).intersection(p5)) == 2:
            five = p5
            numbers_map[5] = set(five)
            linq_list.remove(five)
            break
    # Figure out 2. It's the last one remaining
    five_patterns = linq_list.where(lambda s: len(s) == 5)
    assert len(five_patterns) == 1
    two = five_patterns.first()
    numbers_map[2] = set(two)
    linq_list.remove(two)
    # Figure out 9.
    six_patterns = linq_list.where(lambda s: len(s) == 6)
    assert len(six_patterns) == 3
    for p6 in six_patterns:
        if len(numbers_map[4].difference(p6)) == 0:
            nine = p6
            numbers_map[9] = set(nine)
            linq_list.remove(nine)
            break
    # Figure out 6
    six_patterns = linq_list.where(lambda s: len(s) == 6)
    assert len(six_patterns) == 2
    for p6 in six_patterns:
        if len(numbers_map[5].difference(p6)) == 0:
            six = p6
            numbers_map[6] = set(six)
            linq_list.remove(six)
            break
    # 0 is the only 6 segment pattern left.
    six_patterns = linq_list.where(lambda s: len(s) == 6)
    assert len(six_patterns) == 1
    zero = six_patterns.first()
    numbers_map[0] = set(zero)
    linq_list.remove(zero)
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
