"""Test the bingo problem."""
import pytest
from bingo import puzzle_input_to_bingo, is_board_winner


@pytest.fixture
def raw_data() -> list[str]:
    return """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

    22 13 17 11  0
    8  2 23  4 24
    21  9 14 16  7
    6 10  3 18  5
    1 12 20 15 19

    3 15  0  2 22
    9 18 13 17  5
    19  8  7 25 23
    20 11 10 24  4
    14 21 16 12  6

    14 21 17 24  4
    10 16 15  9 19
    18  8 23 26 20
    22 11 13  6  5
    2  0 12  3  7
    """.splitlines()


def test_puzzle_input_to_bingo(raw_data: list[str]):
    bingo = puzzle_input_to_bingo(raw_data)
    assert bingo.moves[0] == 7 and bingo.moves[-1] == 1
    assert len(bingo.boards) == 3


def test_is_board_winner_no_marked_numbers(raw_data: list[str]):
    bingo = puzzle_input_to_bingo(raw_data)
    assert is_board_winner(bingo.boards[0]) is False


def test_is_board_winner_with_winning_row(raw_data: list[str]):
    bingo = puzzle_input_to_bingo(raw_data)
    for i in range(5):
        bingo.boards[0][i] = -1
    assert is_board_winner(bingo.boards[0]) is True


def test_is_board_winner_with_winning_column(raw_data: list[str]):
    bingo = puzzle_input_to_bingo(raw_data)
    bingo.boards[0][3] = -1
    bingo.boards[0][8] = -1
    bingo.boards[0][13] = -1
    bingo.boards[0][18] = -1
    bingo.boards[0][23] = -1
    assert is_board_winner(bingo.boards[0]) is True
