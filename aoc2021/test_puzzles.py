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
    assert result == 5
