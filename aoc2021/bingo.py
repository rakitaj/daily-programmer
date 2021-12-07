"""Advent of Code Day 4"""
from dataclasses import dataclass


@dataclass
class Bingo:
    moves: list[int]
    boards: list[list[int]]


def puzzle_input_to_bingo(lines: list[str]) -> Bingo:
    moves: list[int] = [int(move) for move in lines[0].split(",")]
    boards: list[list[int]] = list()
    # Start at index 2, line 3 parsing bingo boards.
    i = 2
    while i < len(lines):
        board: list[int] = list()
        for j in range(5):
            numbers = [int(num) for num in lines[i + j].split()]
            board.extend(numbers)
        i += 6
        boards.append(board)
    bingo = Bingo(moves=moves, boards=boards)
    return bingo


def mark_board(board: list[int], drawn_number: int) -> None:
    for i in range(len(board)):
        if board[i] == drawn_number:
            board[i] = -1


def is_board_winner(board: list[int]) -> bool:
    # Check rows
    for i in range(0, len(board), 5):
        indices = range(i, i + 5)
        if all(board[i] == -1 for i in indices) is True:
            return True
    # Check columns
    for i in range(0, 5):
        indices = range(i, len(board), 5)
        if all(board[i] == -1 for i in indices) is True:
            return True
    return False
