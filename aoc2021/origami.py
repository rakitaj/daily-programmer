"""
Solve the Transparent Origami puzzle in Advent Of Code 2021

7, 14 = 0
7, 13 = 1
7, 10 = 4

result = (start - (fold * 2))
"""
from typing import Iterable
from algos import Point, Grid


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


def fold_points(points: Iterable[Point], x_fold: int | None, y_fold: int | None) -> set[Point]:
    folded_points: set[Point] = set()
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
            folded_points.add(Point(x_final, point.y))
        elif y_fold and y_fold < point.y:
            y_final = abs(point.y - (y_fold * 2))
            folded_points.add(Point(point.x, y_final))
        else:
            folded_points.add(Point(point.x, point.y))
    return folded_points


def fold_points_with_fold_list(points: list[Point], folds: list[str], n: int) -> set[Point]:
    folded_points: set[Point] = set(points)
    for i in range(n):
        fold = folds[i]
        main, num_string = fold.split("=")
        num = int(num_string)
        if " x" in main:
            folded_points = fold_points(folded_points, num, None)
        if " y" in main:
            folded_points = fold_points(folded_points, None, num)
    return folded_points


def visualize_origami(points: Iterable[Point]) -> Grid:
    max_x = 0
    max_y = 0
    for p in points:
        max_x = max(p.x, max_x)
        max_y = max(p.y, max_y)
    grid = Grid.as_zeros(max_x + 1, max_y + 1)
    for p in points:
        grid.set(p.x, p.y, 8)
    return grid
