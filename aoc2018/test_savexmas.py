import pytest
from savexmas import common_letters, FabricClaim, Point


@pytest.mark.parametrize("word1, word2, expected", [
    ("abcde", "abcde", "abcde"),
    ("abcd", "abzd", "abd"),
    ("qabc", "rabc", "abc")
])
def test_common_letters(word1, word2, expected):
    result = common_letters(word1, word2)
    assert result == expected


def test_fabric_claim_from_claim_string():
    claim_string = "#123 @ 3,2: 5x4"
    claim = FabricClaim.from_puzzle_input(claim_string)
    assert claim.claim_id == 123
    assert claim.left_padding == 3
    assert claim.top_padding == 2
    assert claim.width == 5
    assert claim.height == 4


@pytest.mark.parametrize("point1, point2, expected", [
    (Point(0, 0), Point(0, 0), True),
    (Point(2, 4), Point(4, 2), False),
    (Point(7, -2), Point(12, 42), False)
])
def test_point_eq(point1: Point, point2: Point, expected: bool):
    result = point1 == point2
    assert result == expected


@pytest.mark.parametrize("point1, point2, expected", [
    (Point(0, 0), Point(0, 0), True),
    (Point(2, 4), Point(4, 2), False),
    (Point(7, -2), Point(12, 42), False),
    (Point(0, 12), Point(12, 0), False),
    (Point(77, 123), Point(77, 123), True)
])
def test_point_hash(point1: Point, point2: Point, expected: bool):
    result = hash(point1) == hash(point2)
    assert result == expected


def test_fabric_claim_points():
    fc = FabricClaim(1, 5, 7, 3, 2)
    points = fc.points()
    # expected_points = [Point(5, 7), Point(6, 7), Point(7, 7), Point(5, 8), Point(6, 8), Point(7, 8)]
    expected_points = {
        Point(5, 7): False,
        Point(6, 7): False,
        Point(7, 7): False,
        Point(5, 8): False,
        Point(6, 8): False,
        Point(7, 8): False
    }
    assert points == expected_points
