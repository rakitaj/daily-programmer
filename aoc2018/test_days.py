"""
Test for the different days 2018.
"""
from aoc2018.xmasdays import day01_1, day01_2, day02_1, day02_2, day03_1


def test_day01_part1():
    assert day01_1() == 502


def test_day01_part2():
    assert day01_2() == 71961


def test_day02_part1():
    assert day02_1() == 7904


def test_day03_part2():
    assert day02_2() == "wugbihckpoymcpaxefotvdzns"


def test_day03_part1():
    assert day03_1() == 113716
