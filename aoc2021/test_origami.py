import pytest
from aoc2021.origami import parse_points, parse_folds, fold_points


@pytest.fixture
def test_data() -> list[str]:
    return """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""".splitlines()


def test_parse_points(test_data: list[str]):
    points = parse_points(test_data)
    assert len(points) == 18


def test_parse_folds(test_data: list[str]):
    folds = parse_folds(test_data)
    assert len(folds) == 2


def test_one_fold(test_data: list[str]):
    points = parse_points(test_data)
    result = fold_points(points, 7, None)
    assert len(result) == 17
