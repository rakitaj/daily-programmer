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
