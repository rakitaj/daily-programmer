"""
Solve the Transparent Origami puzzle in Advent Of Code 2021

7, 14 = 0
7, 13 = 1
7, 10 = 4

result = (start - (fold * 2))
"""
from aoc2021.algos import Point


def parse_points(raw_data: list[str]) -> list[Point]:
    points: list[Point] = list()
    for line in raw_data:
        if "," in line:
            x_raw, y_raw = line.split(",")
            x = int(x_raw)
            y = int(y_raw)
            points.append(Point(x, y))
    return points


def parse_folds(raw_data: list[str]) -> list[str]:
    folds: list[str] = [line for line in raw_data if line.startswith("fold along")]
    return folds


class OrigamiData:
    def __init__(self, points: list[Point], folds: list[str]):
        self.points = points
        self.folds = folds


def fold_points(points: list[Point], x_fold: int | None, y_fold: int | None) -> list[Point]:
    folded_points: list[Point] = list()
    if x_fold and y_fold:
        raise ValueError("One of x_fold or y_fold must be none.")
    for point in points:
        # If the fold is on the line, skip it.
        if x_fold and x_fold == point.x:
            continue
        if y_fold and y_fold == point.y:
            continue
        if x_fold and x_fold < point.x:
            x_final = abs(point.x - (x_fold * 2))
            folded_points.append(Point(x_final, point.y))
        elif y_fold and y_fold < point.y:
            y_final = abs(point.y - (y_fold * 2))
            folded_points.append(Point(point.x, y_final))
        else:
            folded_points.append(Point(point.x, point.y))
        # if x_fold and x_fold != point.x and x_fold < point.x:
        #     x_final = abs(point.x - (x_fold * 2))
        #     folded_points.append(Point(x_final, point.y))
        # if y_fold and y_fold != point.y and y_fold < point.y:
        #     y_final = abs(point.y - (y_fold * 2))
        #     folded_points.append(Point(point.x, y_final))
    return folded_points
