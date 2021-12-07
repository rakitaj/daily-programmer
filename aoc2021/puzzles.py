"""Puzzle solutions for Advent of Code 2021"""
from typing import Callable
from algos import sliding_window, bits_to_decimal, count_bits, most_common_bit
from input_helpers import puzzle_input_to_str, puzzle_input_to_ints
from bingo import puzzle_input_to_bingo, is_board_winner, mark_board


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
    for move in bingo.moves:
        for board in bingo.boards:
            mark_board(board, move)
            if is_board_winner(board) is True:
                board_summed = sum([n for n in board if n != -1])
                return board_summed * move
    return -1


def giant_squid2() -> int:
    puzzle_input = puzzle_input_to_str(4, strip=True)
    bingo = puzzle_input_to_bingo(puzzle_input)
    winning_boards: set[int] = set()
    for move in bingo.moves:
        for iboard in range(len(bingo.boards)):
            mark_board(bingo.boards[iboard], move)
            if is_board_winner(bingo.boards[iboard]) is True:
                winning_boards.add(iboard)
            if len(winning_boards) == len(bingo.boards) - 1:
                i_winning_board = winning_boards.difference(range(len(bingo.boards)))
                breakpoint()
                board_summed = sum([n for n in bingo.boards[i_winning_board] if n != -1])
                return board_summed * move
    return -1


if __name__ == "__main__":
    print(f"Sonar Sweep part 1 {sonar_sweep(sonar_sweep_lookback)}")
    print(f"Sonar Sweep part 2 {sonar_sweep(sonar_sweep_sliding_window)}")
    print(f"Dive part 1 {dive1()}")
    print(f"Dive part 2 {dive2()}")
    print(f"Binary diagnostic 1 {binary_diagnostic1()}")
    print(f"Binary diagnostic 2 {binary_diagnostic2()}")
    print(f"Giant squid 1 {giant_squid1()}")
    print(f"Giant squid 2 {giant_squid2()}")
