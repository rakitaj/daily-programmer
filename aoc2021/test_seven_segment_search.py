import pytest
from seven_segment_search import *


@pytest.fixture
def signal_patterns() -> list[str]:
    return [
        "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
        "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
        "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
        "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
        "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
        "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
        "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
        "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
        "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
        "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
    ]


def test_seven_segment_search(signal_patterns: list[str]):
    result = output_pattern_counts(signal_patterns)
    assert result == 26


def test_unscramble():
    parsed_signal_patterns = parse_signal_patterns(
        ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
    )
    expected: dict[int, set[str]] = {
        8: set("acedgfb"),
        5: set("cdfbe"),
        2: set("gcdfa"),
        3: set("fbcad"),
        7: set("dab"),
        9: set("cefabd"),
        6: set("cdfgeb"),
        4: set("eafb"),
        0: set("cagedb"),
        1: set("ab"),
    }
    result = unscramble(parsed_signal_patterns[0])
    assert result == expected


def test_unscramble_output_pattern():
    parsed_signal_patterns = parse_signal_patterns(
        ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
    )
    result = unscramble_output_pattern(parsed_signal_patterns[0])
    assert result == "5353"


@pytest.mark.skip
def test_sum_all_output_patterns(signal_patterns: list[str]):
    total = 0
    parsed_signal_patterns = parse_signal_patterns(signal_patterns)
    for signal_pattern in parsed_signal_patterns:
        number = unscramble_output_pattern(signal_pattern)
        total += int(number)
    assert total == 61229


@pytest.mark.parametrize(
    "pattern_index, expected",
    [
        (0, 8394),
        (1, 9781),
        (2, 1197),
        (3, 9361),
        (4, 4873),
        (5, 8418),
        (6, 4548),
        (7, 1625),
        (8, 8717),
        (9, 4315),
    ],
)
def test_individual_output_pattern(signal_patterns: list[str], pattern_index: int, expected: int):
    parsed_signal_patterns = parse_signal_patterns(signal_patterns)
    number = unscramble_output_pattern(parsed_signal_patterns[pattern_index])
    assert number == str(expected)
