"""Puzzle solutions for Advent of Code 2021"""
from typing import Callable
from collections import Counter
from algos import sliding_window, bits_to_decimal, count_bits, most_common_bit, Point, diagonal_line, Grid
from seven_segment_search import unscramble_output_pattern, parse_signal_patterns, output_pattern_counts
from input_helpers import puzzle_input_to_str, puzzle_input_to_ints
from bingo import puzzle_input_to_bingo, first_winning_board, last_winning_board
from passagepathing import parse_connections, find_paths
from origami import parse_folds, parse_points, fold_points_with_fold_list, visualize_origami


def sonar_sweep(logic_func: Callable[[list[int]], float]):
    depth_measurements = puzzle_input_to_ints(1)
    result = logic_func(depth_measurements)
    return result


def sonar_sweep_lookback(depths: list[int]) -> int:
    count = 0
    for i in range(1, len(depths)):
        if depths[i - 1] < depths[i]:
            count += 1
    return count


def sonar_sweep_sliding_window(depths: list[int]) -> int:
    count = 0
    prev_window_total = 1000000
    for i in range(2, len(depths)):
        window_total = sliding_window(depths, i, 3)
        if prev_window_total < window_total:
            count += 1
        prev_window_total = window_total
    return count


def dive1():
    positions = puzzle_input_to_str(2)
    x = 0
    depth = 0
    for position in positions:
        direction, magnitude = position.split()
        magnitude = int(magnitude)
        if direction == "forward":
            x += magnitude
        if direction == "down":
            depth += magnitude
        if direction == "up":
            depth -= magnitude
    return x * depth


def dive2():
    positions = puzzle_input_to_str(2)
    x = 0
    depth = 0
    aim = 0
    for position in positions:
        direction, magnitude = position.split()
        magnitude = int(magnitude)
        if direction == "forward":
            x += magnitude
            depth += aim * magnitude
        if direction == "down":
            aim += magnitude
        if direction == "up":
            aim -= magnitude
    return x * depth


def binary_diagnostic1():
    bits_list = puzzle_input_to_str(3, strip=True)
    gamma_rate_bits: list[int] = list()
    for i in range(len(bits_list[0])):
        gamma_rate_bits.append(most_common_bit(bits_list, i))
    eplison_rate_bits = [bit ^ 1 for bit in gamma_rate_bits]
    gamma_rate_decimal = bits_to_decimal(gamma_rate_bits, "big")
    epsilon_rate_decimal = bits_to_decimal(eplison_rate_bits, "big")
    return gamma_rate_decimal * epsilon_rate_decimal


def binary_diagnostic2() -> int:
    bits_list = puzzle_input_to_str(3, strip=True)
    oxygen_generator_rating = calculate_oxygen_generator_rating(bits_list.copy())
    co2_scrubber_rating = calculate_co2_scrubber_rating(bits_list.copy())
    return oxygen_generator_rating * co2_scrubber_rating


def calculate_oxygen_generator_rating(bits_list: list[str]) -> int:
    length = len(bits_list[0])
    for i in range(length):
        bits_count = count_bits(bits_list, i)
        if bits_count[0] <= bits_count[1]:
            bits_list = [bits for bits in bits_list if bits[i] == "1"]
        else:
            bits_list = [bits for bits in bits_list if bits[i] == "0"]
        if len(bits_list) == 1:
            break
    bits_ready_to_convert: list[int] = [int(bit) for bit in bits_list[0]]
    return bits_to_decimal(bits_ready_to_convert, "big")


def calculate_co2_scrubber_rating(bits_list: list[str]) -> int:
    length = len(bits_list[0])
    for i in range(length):
        bits_count = count_bits(bits_list, i)
        if bits_count[0] <= bits_count[1]:
            bits_list = [bits for bits in bits_list if bits[i] == "0"]
        else:
            bits_list = [bits for bits in bits_list if bits[i] == "1"]
        if len(bits_list) == 1:
            break
    bits_ready_to_convert: list[int] = [int(bit) for bit in bits_list[0]]
    return bits_to_decimal(bits_ready_to_convert, "big")


def giant_squid1() -> int:
    puzzle_input = puzzle_input_to_str(4, strip=True)
    bingo = puzzle_input_to_bingo(puzzle_input)
    return first_winning_board(bingo)


def giant_squid2() -> int:
    puzzle_input = puzzle_input_to_str(4, strip=True)
    bingo = puzzle_input_to_bingo(puzzle_input)
    return last_winning_board(bingo)


def parse_vent_line(vent_line: str) -> tuple[Point, Point]:
    start, end = vent_line.split("->")
    x1, y1 = start.split(",")
    x2, y2 = end.split(",")
    start_point = Point(int(x1), int(y1))
    end_point = Point(int(x2), int(y2))
    return (start_point, end_point)


def normalize_vents(vent_vectors: list[tuple[Point, Point]]) -> list[tuple[Point, Point]]:
    result: list[tuple[Point, Point]] = list()
    for vector in vent_vectors:
        start, end = vector
        start_point = min((start.x, start.y), (end.x, end.y))
        end_point = max((start.x, start.y), (end.x, end.y))
        ordered_vector = (Point(start_point[0], start_point[1]), Point(end_point[0], end_point[1]))
        result.append(ordered_vector)
    return result


def only_straight_lines(vent_vectors: list[tuple[Point, Point]]) -> list[tuple[Point, Point]]:
    result: list[tuple[Point, Point]] = list()
    for vector in vent_vectors:
        start, end = vector
        if start.x == end.x or start.y == end.y:
            result.append(vector)
    return result


def hydrothermal_venture(vent_vectors: list[tuple[Point, Point]]) -> int:
    occupied_points: dict[tuple[int, int], int] = dict()
    ordered_vectors = normalize_vents(vent_vectors)
    # Need to trim and normalize vectors because sometimes the end is the first point and the start is the second.
    for vector in ordered_vectors:
        start, end = vector
        if start.x == end.x:
            for y in range(start.y, end.y + 1):
                if (start.x, y) in occupied_points:
                    occupied_points[(start.x, y)] += 1
                else:
                    occupied_points[(start.x, y)] = 1
        elif start.y == end.y:
            for x in range(start.x, end.x + 1):
                if (x, start.y) in occupied_points:
                    occupied_points[(x, start.y)] += 1
                else:
                    occupied_points[(x, start.y)] = 1
        else:
            diagonal_points = diagonal_line(start, end)
            for point in diagonal_points:
                if point in occupied_points:
                    occupied_points[point] += 1
                else:
                    occupied_points[point] = 1
    overlap_count = 0
    for _, value in occupied_points.items():
        if 2 <= value:
            overlap_count += 1
    return overlap_count


def hydrothermal_venture1() -> int:
    puzzle_input = puzzle_input_to_str(5, True)
    vent_vectors = [parse_vent_line(vent_line) for vent_line in puzzle_input]
    vent_vectors = only_straight_lines(vent_vectors)
    result = hydrothermal_venture(vent_vectors)
    return result


def hydrothermal_venture2() -> int:
    puzzle_input = puzzle_input_to_str(5, True)
    vent_vectors = [parse_vent_line(vent_line) for vent_line in puzzle_input]
    result = hydrothermal_venture(vent_vectors)
    return result


def parse_lantern_fish_list(puzzle_input: str) -> dict[int, int]:
    fish_life_numbers = [int(fish) for fish in puzzle_input.split(",")]
    fish_lives: dict[int, int] = dict()
    for fish in fish_life_numbers:
        if fish in fish_lives:
            fish_lives[fish] += 1
        else:
            fish_lives[fish] = 1
    return fish_lives


def lantern_fish_tick(fish_dict: dict[int, int]) -> dict[int, int]:
    new_fish_dict: dict[int, int] = dict()
    for i in range(8, -1, -1):
        if i == 0:
            new_fish_dict[8] = fish_dict.get(i, 0)
            new_fish_dict[6] += fish_dict.get(i, 0)
        else:
            new_fish_dict[i - 1] = fish_dict.get(i, 0)
    return new_fish_dict


def lantern_fish(num_ticks: int):
    data = puzzle_input_to_str(6, True)
    fish_dict = parse_lantern_fish_list(data[0])
    for _ in range(num_ticks):
        fish_dict = lantern_fish_tick(fish_dict)
    total = sum(fish_dict.values())
    return total


def minimum_fuel(crab_positions: list[int], cost_function: Callable[[int, int], int]) -> tuple[int, int]:
    best_position = 0
    min_fuel_used = 1_000_000_000_000
    for i in range(min(crab_positions), max(crab_positions) + 1):
        total_fuel = 0
        for crab_position in crab_positions:
            fuel_needed = cost_function(crab_position, i)
            total_fuel += fuel_needed
        if total_fuel < min_fuel_used:
            min_fuel_used = total_fuel
            best_position = i
    return (best_position, min_fuel_used)


def linear_crab_fuel(istart: int, itarget: int) -> int:
    return abs(itarget - istart)


cached_nonlinear_fuel: dict[int, int] = {}


def nonlinear_crab_fuel(istart: int, itarget: int) -> int:
    diff = abs(itarget - istart)
    total = 0
    if diff not in cached_nonlinear_fuel:
        cached_nonlinear_fuel[diff] = sum(range(diff + 1))
    total += cached_nonlinear_fuel[diff]
    return total


def the_treachery_of_whales(cost_function: Callable[[int, int], int]) -> int:
    puzzle_input = puzzle_input_to_str(7)
    crab_positions = [int(x) for x in puzzle_input[0].split(",")]
    _, min_fuel = minimum_fuel(crab_positions, cost_function)
    return min_fuel


def seven_segment_search_1() -> int:
    puzzle_input = puzzle_input_to_str(8)
    result = output_pattern_counts(puzzle_input)
    return result


def seven_segment_search_2() -> int:
    total = 0
    puzzle_input = puzzle_input_to_str(8)
    signal_patterns = parse_signal_patterns(puzzle_input)
    for signal_pattern in signal_patterns:
        number = unscramble_output_pattern(signal_pattern)
        total += int(number)
    return total


def parse_smoke_basin_string(smoke_basin_strings: list[str]) -> list[list[int]]:
    result: list[list[int]] = list()
    for line in smoke_basin_strings:
        nums = [int(char) for char in line.strip()]
        result.append(nums)
    return result


def smoke_low_points(grid: Grid) -> list[int]:
    low_points: list[int] = list()
    for y in range(grid.y_length):
        for x in range(grid.x_length):
            min_point = grid.get(x, y)
            if min_point is None:
                continue
            neighbors = grid.get_neighbor_values(x, y)
            if all_neighbors_gt(min_point, neighbors):
                low_points.append(min_point)
    return low_points


def any_neighbors_lt_or_eq(target: int, neighbors: list[int]) -> bool:
    for n in neighbors:
        if n <= target:
            return True
    return False


def all_neighbors_gt(target: int, neighbors: list[int]) -> bool:
    for n in neighbors:
        if n <= target:
            return False
    return True


def smoke_low_basins(grid: Grid) -> list[int]:
    """
    Calculate the size of every basin.

    :param grid: Grid of ints representing the smoke heights.
    :returns: A list of the size of every basin, unordered.
    """
    basins: list[int] = list()
    visited: set[tuple[int, int]] = set()
    for x in range(grid.x_length):
        for y in range(grid.y_length):
            if (x, y) in visited or grid.get(x, y) == 9:
                continue
            basin_visited = depth_first_search((x, y), grid)
            basins.append(len(basin_visited))
            visited.update(basin_visited)
    return basins


def depth_first_search(starting_point: tuple[int, int], grid: Grid) -> set[tuple[int, int]]:
    """Perform a depth first search to find a smoke basin."""
    visited: set[tuple[int, int]] = set()
    queue: list[tuple[int, int]] = [starting_point]
    if starting_point in visited or grid.get(starting_point[0], starting_point[1]) == 9:
        return set()
    while 0 < len(queue):
        x, y = queue.pop(0)

        up = (x, y + 1)
        down = (x, y - 1)
        left = (x - 1, y)
        right = (x + 1, y)

        if grid.get(up[0], up[1]) is not None and grid.get(up[0], up[1]) != 9 and up not in visited:
            visited.add(up)
            queue.append(up)
        if grid.get(down[0], down[1]) is not None and grid.get(down[0], down[1]) != 9 and down not in visited:
            visited.add(down)
            queue.append(down)
        if grid.get(left[0], left[1]) is not None and grid.get(left[0], left[1]) != 9 and left not in visited:
            visited.add(left)
            queue.append(left)
        if (
            grid.get(right[0], right[1]) is not None
            and grid.get(right[0], right[1]) != 9
            and right not in visited
        ):
            visited.add(right)
            queue.append(right)
    return visited


def smoke_basin_1():
    puzzle_input = puzzle_input_to_str(9)
    numbers = parse_smoke_basin_string(puzzle_input)
    grid = Grid(numbers)
    low_points = smoke_low_points(grid)
    total = 0
    for p in low_points:
        total += p + 1
    return total


def smoke_basin_2():
    puzzle_input = puzzle_input_to_str(9)
    numbers = parse_smoke_basin_string(puzzle_input)
    grid = Grid(numbers)
    low_basins = smoke_low_basins(grid)
    ordered_basins = sorted(low_basins)
    return ordered_basins[-1] * ordered_basins[-2] * ordered_basins[-3]


def syntax_parser(line: str) -> str:
    """Check that lines are not corrupted."""
    char_map: dict[str, str] = {")": "(", "]": "[", "}": "{", ">": "<"}
    stack: list[str] = list()
    for char in line:
        if char in ["(", "[", "{", "<"]:
            stack.append(char)
        elif stack[-1] == char_map[char]:
            stack.pop()
        else:
            return char
    return ""


def syntax_autocomplete(line: str) -> list[str]:
    opening_char_map: dict[str, str] = {"(": ")", "[": "]", "{": "}", "<": ">"}
    closing_char_map: dict[str, str] = {")": "(", "]": "[", "}": "{", ">": "<"}
    stack: list[str] = list()
    autocomplete: list[str] = list()
    for char in line:
        if char in opening_char_map.keys():
            stack.append(char)
        elif stack[-1] == closing_char_map[char]:
            stack.pop()
    for i in range(len(stack) - 1, -1, -1):
        autocomplete.append(opening_char_map[stack[i]])
    return autocomplete


def syntax_scoring_1():
    puzzle_input = puzzle_input_to_str(10, strip=True)
    closing_char_map: dict[str, int] = {")": 3, "]": 57, "}": 1197, ">": 25137, "": 0}
    total = 0
    for line in puzzle_input:
        illegal_char = syntax_parser(line)
        score = closing_char_map[illegal_char]
        total += score
    return total


def score_autocomplete(chars: list[str]) -> int:
    total = 0
    points = {")": 1, "]": 2, "}": 3, ">": 4}
    for char in chars:
        total = total * 5
        total += points[char]
    return total


def syntax_scoring_2():
    puzzle_input = puzzle_input_to_str(10, strip=True)
    scores: list[int] = list()
    for line in puzzle_input:
        illegal_character = syntax_parser(line)
        if illegal_character != "":
            continue
        autocomplete_chars = syntax_autocomplete(line)
        score = score_autocomplete(autocomplete_chars)
        scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]


def passage_pathing_1() -> int:
    puzzle_input = puzzle_input_to_str(12, strip=True)
    connections = parse_connections(puzzle_input)
    paths = find_paths(connections)
    return len(paths)


def transparent_origami_1() -> int:
    puzzle_input = puzzle_input_to_str(13, strip=True)
    points = parse_points(puzzle_input)
    folds = parse_folds(puzzle_input)
    result = fold_points_with_fold_list(points, folds, 1)
    return len(result)


def transparent_origami_2() -> str:
    puzzle_input = puzzle_input_to_str(13, strip=True)
    points = parse_points(puzzle_input)
    folds = parse_folds(puzzle_input)
    result = fold_points_with_fold_list(points, folds, len(folds))
    viz = visualize_origami(result)
    return str(viz)


def parse_polymerization(lines: list[str]) -> tuple[str, dict[str, str]]:
    template = lines[0].strip()
    patterns: dict[str, str] = dict()
    for line in lines[2:]:
        parts = line.split("->")
        patterns[parts[0].strip()] = parts[1].strip()
    return (template, patterns)


def polymerization2(template: str, patterns: dict[str, str], n: int) -> dict[str, int]:
    pairs: dict[str, int] = dict()
    for i in range(len(template) - 1):
        pairs.setdefault(template[i : i + 2], 1)
    for _ in range(n + 1):
        pairs = polymerization_tick(pairs, patterns)
    counts: dict[str, int] = dict()
    for p in pairs:
        counts.setdefault(p[0], 0)
        counts[p[0]] += 1
        counts.setdefault(p[1], 0)
        counts[p[1]] += 1
    return counts


def polymerization_tick(pairs: dict[str, int], patterns: dict[str, str]) -> dict[str, int]:
    ticked_pairs: dict[str, int] = dict()
    for pair in pairs:
        if pair in patterns:
            p1 = pair[0] + patterns[pair]
            ticked_pairs.setdefault(p1, 0)
            ticked_pairs[p1] += 1

            p2 = patterns[pair] + pair[1]
            ticked_pairs.setdefault(p2, 0)
            ticked_pairs[p2] += 1
    return ticked_pairs


def polymerization(template: str, patterns: dict[str, str]) -> str:
    i = 0
    length = len(template)
    while i < length:
        pair = template[i : i + 2]
        if pair in patterns:
            template = template[: i + 1] + patterns[pair] + template[i + 1 :]
            i += 1
            length += 1
        i += 1
    return template


def polymerization_loop(template: str, patterns: dict[str, str], n: int) -> str:
    for _ in range(n):
        # print(len(template))
        template = polymerization(template, patterns)
    return template


def extended_polymerization(n: int):
    puzzle_input = puzzle_input_to_str(14)
    template, patterns = parse_polymerization(puzzle_input)
    final_string = polymerization_loop(template, patterns, n)

    counts = Counter(final_string)
    commonality_list = counts.most_common()
    return commonality_list[0][1] - commonality_list[-1][1]


if __name__ == "__main__":
    print(f"Sonar Sweep part 1 {sonar_sweep(sonar_sweep_lookback)}")
    print(f"Sonar Sweep part 2 {sonar_sweep(sonar_sweep_sliding_window)}")
    print(f"Dive part 1 {dive1()}")
    print(f"Dive part 2 {dive2()}")
    print(f"Binary diagnostic 1 {binary_diagnostic1()}")
    print(f"Binary diagnostic 2 {binary_diagnostic2()}")
    print(f"Giant squid 1 {giant_squid1()}")
    print(f"Giant squid 2 {giant_squid2()}")
    print(f"Hydrothermal Venture 1 {hydrothermal_venture1()}")
    print(f"Hydrothermal Venture 2 {hydrothermal_venture2()}")
    print(f"Lantern Fish 1 {lantern_fish(80)}")
    print(f"Lantern Fish 2 {lantern_fish(256)}")
    print(f"The Treachery of Whales 1 {the_treachery_of_whales(linear_crab_fuel)}")
    print(f"The Treachery of Whales 2 {the_treachery_of_whales(nonlinear_crab_fuel)}")
    print(f"Seven Segment Search 1 {seven_segment_search_1()}")
    print(f"Seven Segment Search 2 {seven_segment_search_2()}")
    print(f"Smoke Basin 1 {smoke_basin_1()}")
    print(f"Smoke Basin 2 {smoke_basin_2()}")
    print(f"Syntax Scoring 1 {syntax_scoring_1()}")
    print(f"Syntax Scoring 2 {syntax_scoring_2()}")
    print(f"Passage Pathing 1 {passage_pathing_1()}")
    print(f"Transparent Origami 1 {transparent_origami_1()}")
    print(f"Transparent Origami 2 {transparent_origami_2()}")
    print(f"Extended Polymerization 1 {extended_polymerization(10)}")
    print(f"Extended Polymerization 2 {extended_polymerization(14)}")
    # import cProfile

    # cProfile.run("extended_polymerization(14)")
