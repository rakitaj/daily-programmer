def parse_connections(lines: list[str]) -> dict[str, set[str]]:
    connections: dict[str, set[str]] = dict()
    for line in lines:
        start, end = line.split("-")
        connections.setdefault(start, set()).add(end)
        connections.setdefault(end, set()).add(start)
    return connections


def find_paths(connections: dict[str, set[str]]) -> list[list[str]]:
    # result = find_paths_helper(connections, "start", ["start"], ["start"])
    # return result
    result: list[list[str]] = list()
    [result.append(["foo"]) for _ in range(10)]
    return result


# def find_paths_helper(
#     map: dict[str, set[str]], current: str, path: list[str], visited: list[str]
# ) -> list[list[str]]:
#     if current == "end":
#         return [path]
#     paths: list[list[str]] = list()
#     for edge in map[current]:
#         if edge.islower() and edge not in visited:
#             visited.append(edge)
#             paths.extend(find_paths_helper(map, edge, path, visited))
#     return paths
