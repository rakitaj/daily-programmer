"""Tests the puzzles in Advent of Code 2021 along with some test for helper function and algorithms."""
import pytest
from test_algos import bits_list, Point
from puzzles import *


@pytest.fixture
def vents_list() -> list[str]:
    return [
        "0,9 -> 5,9",
        "8,0 -> 0,8",
        "9,4 -> 3,4",
        "2,2 -> 2,1",
        "7,0 -> 7,4",
        "6,4 -> 2,0",
        "0,9 -> 2,9",
        "3,4 -> 1,4",
        "0,0 -> 8,8",
        "5,5 -> 8,2",
    ]


@pytest.fixture
def smoke_basin_string() -> list[str]:
    return """2199943210
        3987894921
        9856789892
        8767896789
        9899965678""".splitlines()


def test_sonar_sweep_simple():
    depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert sonar_sweep_lookback(depths) == 7


def test_sonar_sweep_sliding_window():
    depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert sonar_sweep_sliding_window(depths) == 5


def test_calculate_oxygen_generator_rating(bits_list: list[str]):
    assert calculate_oxygen_generator_rating(bits_list) == 23


def test_calculate_co2_scrubber_rating(bits_list: list[str]):
    assert calculate_co2_scrubber_rating(bits_list) == 10


def test_parse_vent_line(vents_list: list[str]):
    result = parse_vent_line(vent_line=vents_list[0])
    assert (Point(0, 9), Point(5, 9)) == result


def test_normalize_vents_only_straight_lines(vents_list: list[str]):
    vent_vectors = [parse_vent_line(vent_line) for vent_line in vents_list]
    vent_vectors = only_straight_lines(vent_vectors)
    result = normalize_vents(vent_vectors)
    assert result == [
        (Point(0, 9), Point(5, 9)),
        (Point(3, 4), Point(9, 4)),
        (Point(2, 1), Point(2, 2)),
        (Point(7, 0), Point(7, 4)),
        (Point(0, 9), Point(2, 9)),
        (Point(1, 4), Point(3, 4)),
    ]


def test_hydrothermal_venture(vents_list: list[str]):
    vent_vectors = [parse_vent_line(vent_line) for vent_line in vents_list]
    result = hydrothermal_venture(vent_vectors)
    assert result == 12


def test_parse_lantern_fish_list():
    data = "3,4,3,1,2"
    fish_dict = parse_lantern_fish_list(data)
    assert fish_dict == {1: 1, 1: 1, 2: 1, 3: 2, 4: 1}


def test_lantern_fish_tick():
    fish_dict = parse_lantern_fish_list("3,4,3,1,2")
    result = lantern_fish_tick(fish_dict)
    result = dict_remove_empty_kvps(result, 0)
    assert result == {2: 2, 0: 1, 1: 1, 3: 1}


@pytest.mark.parametrize(
    "num_ticks, expected",
    [(3, {0: 2, 1: 1, 5: 1, 6: 1, 7: 1, 8: 1}), (18, {6: 5, 0: 3, 4: 2, 5: 1, 1: 5, 2: 3, 3: 2, 7: 1, 8: 4})],
)
def test_lantern_fish_tick_3(num_ticks: int, expected: dict[int, int]):
    fish_dict = parse_lantern_fish_list("3,4,3,1,2")
    for _ in range(num_ticks):
        fish_dict = lantern_fish_tick(fish_dict)
    fish_dict = dict_remove_empty_kvps(fish_dict, 0)
    assert fish_dict == expected


def dict_remove_empty_kvps(dictionary: dict[int, int], value_value: int) -> dict[int, int]:
    trimmed_dict: dict[int, int] = dict()
    for key, value in dictionary.items():
        if value != value_value:
            trimmed_dict[key] = value
    return trimmed_dict


def test_minimum_fuel_linear_cost():
    crab_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert minimum_fuel(crab_positions, linear_crab_fuel) == (2, 37)


def test_minimum_fuel_nonlinear_cost():
    crab_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert minimum_fuel(crab_positions, nonlinear_crab_fuel) == (5, 168)


def test_smoke_low_points(smoke_basin_string: list[str]):
    numbers = parse_smoke_basin_string(smoke_basin_string)
    grid = Grid(numbers)
    low_points = smoke_low_points(grid)
    assert low_points == [1, 0, 5, 5]


def test_smoke_low_basins(smoke_basin_string: list[str]):
    numbers = parse_smoke_basin_string(smoke_basin_string)
    grid = Grid(numbers)
    low_basins = smoke_low_basins(grid)
    basins_sorted = sorted(low_basins)
    assert basins_sorted[-1] == 14 and basins_sorted[-2] == 9 and basins_sorted[-3] == 9


@pytest.mark.parametrize(
    "line, expected",
    [
        ("{([(<{}[<>[]}>{[]{[(<()>", "}"),
        ("[[<[([]))<([[{}[[()]]]", ")"),
        ("[{[{({}]{}}([{[{{{}}([]", "]"),
        ("[<(<(<(<{}))><([]([]()", ")"),
        ("<{([([[(<>()){}]>(<<{{", ">"),
    ],
)
def test_syntax_parser(line: str, expected: int):
    illegal_char = syntax_parser(line)
    assert illegal_char == expected
