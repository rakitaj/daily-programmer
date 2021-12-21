import pytest
from algos import *


@pytest.fixture
def bits_list() -> list[str]:
    return [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]


@pytest.fixture
def linq_list() -> LinqList[str]:
    data: LinqList[str] = LinqList()
    data.append("one")
    data.append("two twos")
    data.append("two twos")
    data.append("one three")
    return data


@pytest.mark.parametrize("start, lookback, expected", [(0, 1, 199), (2, 3, 607), (3, 3, 618)])
def test_sliding_window(start: int, lookback: int, expected: float):
    nums = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert expected == sliding_window(nums, start, lookback)


@pytest.mark.parametrize("position, expected", [(0, 1), (1, 0), (2, 1), (3, 1), (4, 0)])
def test_most_common_bit(bits_list: list[str], position: int, expected: int):
    assert most_common_bit(bits_list, position) == expected


@pytest.mark.parametrize("bits, decimal", [([1, 0, 1, 1, 0], 22)])
def test_bits_to_decimal(bits: list[int], decimal: int):
    assert bits_to_decimal(bits, "big") == decimal


@pytest.mark.parametrize("start, end, expected", [((0, 0), (0, 0), True), ((0, 5), (5, 0), False)])
def test_point(start: tuple[int, int], end: tuple[int, int], expected: bool):
    point1 = Point(start[0], start[1])
    point2 = Point(end[0], end[1])
    assert (point1 == point2) is expected


def test_diagonal_line():
    start = (1, 1)
    end = (3, 3)
    points = diagonal_line(Point(*start), Point(*end))
    assert len(points) == 3
    assert points[0] == (1, 1) and points[2] == (3, 3)


def test_linq_list_first(linq_list: LinqList[str]):
    assert linq_list.first() == "one"


def test_linq_list_empty_first():
    empty_linq_list: LinqList[int] = LinqList()
    with pytest.raises(IndexError):
        empty_linq_list.first()


def test_linq_list_single(linq_list: LinqList[str]):
    assert linq_list.single(lambda s: s == "one three") == "one three"


def test_linq_list_single_matches_multiple(linq_list: LinqList[str]):
    with pytest.raises(Exception):
        linq_list.single(lambda s: s == "two twos")


def test_linq_list_where_matches(linq_list: LinqList[str]):
    results = linq_list.where(lambda s: s == "two twos")
    assert len(results) == 2 and results[0] == "two twos" and results[1] == "two twos"


def test_linq_list_where_no_matches(linq_list: LinqList[str]):
    results = linq_list.where(lambda s: s == "hearts")
    assert len(results) == 0


@pytest.mark.parametrize("x, y", [(-1, -1), (3, 4), (4, 3), (2, 4)])
def test_grid_get_none(x: int, y: int):
    numbers = [[2, 2, 4], [4, 10, 10], [7, 8, 9]]
    grid = Grid(numbers)
    assert grid.get(x, y) is None


@pytest.mark.parametrize("x, y, expected", [(0, 0, 2), (2, 0, 4), (2, 1, 10), (2, 2, 9)])
def test_grid_get(x: int, y: int, expected: int):
    numbers = [[2, 2, 4], [4, 10, 10], [7, 8, 9]]
    grid = Grid(numbers)
    assert grid.get(x, y) == expected
