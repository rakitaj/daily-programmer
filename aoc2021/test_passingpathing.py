import pytest
from typing import Callable
from aoc2021.passagepathing import find_paths, parse_connections, find_paths_advanced


@pytest.fixture
def few_raw_connections() -> list[str]:
    return """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".splitlines()


@pytest.fixture
def medium_raw_connections() -> list[str]:
    return """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""".splitlines()


@pytest.fixture
def large_raw_connetions() -> list[str]:
    return """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""".splitlines()


def test_parse_connections(few_raw_connections: list[str]):
    connections = parse_connections(few_raw_connections)
    assert connections["start"] == {"A", "b"}
    assert connections["A"] == {"c", "start", "b", "end"}
    assert connections["c"] == {"A"}


@pytest.mark.skip
@pytest.mark.parametrize("pathfinding_algo, expected", [(find_paths, 10), (find_paths_advanced, 36)])
def test_pathfinding_with_few_caves(
    few_raw_connections: list[str],
    pathfinding_algo: Callable[[dict[str, set[str]]], list[list[str]]],
    expected: int,
):
    connections = parse_connections(few_raw_connections)
    paths = pathfinding_algo(connections)
    assert len(paths) == expected, pretty_print_paths(paths)


@pytest.mark.skip
@pytest.mark.parametrize("pathfinding_algo, expected", [(find_paths, 19), (find_paths_advanced, 103)])
def test_pathfinding_with_medium_caves(
    medium_raw_connections: list[str],
    pathfinding_algo: Callable[[dict[str, set[str]]], list[list[str]]],
    expected: int,
):
    connections = parse_connections(medium_raw_connections)
    paths = pathfinding_algo(connections)
    paths_string: str = ""
    for p in paths:
        paths_string += "-".join(p) + "\n"
    assert len(paths) == expected, pretty_print_paths(paths)


def test_pathfinding_with_large_caves(large_raw_connetions: list[str]):
    connections = parse_connections(large_raw_connetions)
    paths = find_paths(connections)
    paths_string: str = ""
    for p in paths:
        paths_string += "-".join(p) + "\n"
    assert len(paths) == 226, pretty_print_paths(paths)


def pretty_print_paths(paths: list[list[str]]) -> str:
    paths_string: str = ""
    for p in paths:
        paths_string += "-".join(p) + "\n"
    return paths_string
