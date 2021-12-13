"""Puzzle solutions for Advent of Code 2021"""
from typing import Callable
from algos import sliding_window, bits_to_decimal, count_bits, most_common_bit, Point, diagonal_line
from input_helpers import puzzle_input_to_str, puzzle_input_to_ints
from bingo import puzzle_input_to_bingo, first_winning_board, last_winning_board


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
    best_position, min_fuel = minimum_fuel(crab_positions, cost_function)
    return min_fuel


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
