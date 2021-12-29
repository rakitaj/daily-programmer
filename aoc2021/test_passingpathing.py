import pytest
from aoc2021.passagepathing import find_paths, parse_connections


@pytest.fixture
def small_raw_connections():
    return """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".splitlines()


def test_parse_connections(small_raw_connections: list[str]):
    connections = parse_connections(small_raw_connections)
    assert connections["start"] == {"A", "b"}
    assert connections["A"] == {"c", "start", "b", "end"}
    assert connections["c"] == {"A"}


def test_pathfinding(small_raw_connections: list[str]):
    connections = parse_connections(small_raw_connections)
    paths = find_paths(connections)
    assert len(paths) == 10
