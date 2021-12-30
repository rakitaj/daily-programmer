def parse_connections(lines: list[str]) -> dict[str, set[str]]:
    connections: dict[str, set[str]] = dict()
    for line in lines:
        start, end = line.split("-")
        connections.setdefault(start, set()).add(end)
        connections.setdefault(end, set()).add(start)
    return connections


def find_paths(connections: dict[str, set[str]]) -> list[list[str]]:
    path_finder = PathFinder(connections)
    path_finder.calculate_paths()
    return path_finder.paths


def find_paths_advanced(connections: dict[str, set[str]]) -> list[list[str]]:
    path_finder = PathFinder(connections)
    path_finder.calculate_paths_2()
    return path_finder.paths


class PathFinder:
    def __init__(self, map: dict[str, set[str]]):
        self.map = map
        self.paths: list[list[str]] = list()

    def calculate_paths(self):
        self.calculate_path(["start"], {"start"})

    def calculate_path(self, path: list[str], visited: set[str]):
        # Last node in the path is the current one
        current = path[-1]
        if current == "end":
            self.paths.append(path.copy())
            return
        visited.add(current)
        for edge in self.map[current]:
            if edge.islower() and edge in visited:
                continue
            path.append(edge)
            self.calculate_path(path.copy(), visited.copy())
        visited.remove(current)

    def calculate_paths_2(self):
        self.calculate_path_2(["start"], {"start": 1})

    def calculate_path_2(self, path: list[str], visited: dict[str, int]):
        current = path[-1]
        if current == "end":
            self.paths.append(path.copy())
            return
        visited.setdefault(current, 0)
        visited[current] += 1
        for edge in self.map[current]:
            # If next move is not valid, skip it.
            if not is_next_move_valid(edge, visited):
                continue
            path.append(edge)
            self.calculate_path_2(path.copy(), visited.copy())
        del visited[current]


def is_next_move_valid(next_move: str, counts: dict[str, int]) -> bool:
    """Is the cave the start or end cave? Has any lowercase cave except start or end been visited twice?"""
    if next_move in ["start", "end"]:
        return False
    for key, value in counts.items():
        if key in ["start", "end"]:
            continue
        if 2 <= value:
            return False
    return True
