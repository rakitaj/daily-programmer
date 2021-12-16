from dataclasses import dataclass


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


def unscramble(patterns: list[str]) -> dict[str, str]:
    pattern_map = {"a": "-", "b": "-", "c": "-", "d": "-", "e": "-", "f": "-", "g": "-"}
    pass
