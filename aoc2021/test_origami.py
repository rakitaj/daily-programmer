from algos import Point
from input_helpers import DataType, file_loader
from origami import parse_points, parse_folds, fold_points, visualize_origami


def origami_to_points(lines: list[str]) -> list[Point]:
    points: list[Point] = list()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                points.append(Point(x, y))
    return points


def test_parse_points():
    raw_data = file_loader("day13-smallinput.txt", DataType.TEST)
    points = parse_points(raw_data)
    assert len(points) == 18


def test_parse_folds():
    raw_data = file_loader("day13-smallinput.txt", DataType.TEST)
    folds = parse_folds(raw_data)
    assert len(folds) == 2


def test_one_fold():
    raw_data = file_loader("day13-smallinput.txt", DataType.TEST)
    points = parse_points(raw_data)
    result = fold_points(points, None, 7)
    assert len(result) == 17


def test_two_folds():
    raw_data = file_loader("day13-smallinput.txt", DataType.TEST)
    points = parse_points(raw_data)
    points = fold_points(points, None, 7)
    points = fold_points(points, 5, None)
    assert len(points) == 16


def test_visualize():
    raw_data = file_loader("day13-smallinput.txt", DataType.TEST)
    points = parse_points(raw_data)
    points = fold_points(points, None, 7)
    points = fold_points(points, 5, None)
    grid = visualize_origami(points)
    assert (
        str(grid)
        == """
88888
80008
80008
80008
88888
"""
    )
