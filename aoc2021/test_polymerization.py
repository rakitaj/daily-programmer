import pytest
from collections import Counter
from aoc2021.puzzles import polymerization2
from puzzles import polymerization, polymerization_loop, parse_polymerization
from input_helpers import file_loader, DataType


def test_polymerization():
    data = file_loader("day14.txt", DataType.TEST)
    template, patterns = parse_polymerization(data)
    final_string = polymerization(template, patterns)
    assert final_string == "NCNBCHB"


def test_polymerization_loop():
    data = file_loader("day14.txt", DataType.TEST)
    template, patterns = parse_polymerization(data)
    final_string = polymerization_loop(template, patterns, 4)
    assert final_string == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"


@pytest.mark.skip
def test_polymerization_2():
    data = file_loader("day14.txt", DataType.TEST)
    template, patterns = parse_polymerization(data)
    counts = polymerization2(template, patterns, 1)
    assert counts == {"N": 2, "C": 2, "B": 2, "H": 1}


def test_extended_polymerization():
    data = file_loader("day14.txt", DataType.TEST)
    template, patterns = parse_polymerization(data)
    final_string = polymerization_loop(template, patterns, 16)
    counts: Counter[str] = Counter(final_string)
    commonality_list = counts.most_common()
    assert 117020 == commonality_list[0][1] - commonality_list[-1][1]
