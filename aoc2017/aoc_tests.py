import pytest
import day01

def test_day01_part1():
    sample_inputs = [(1122, 3), (1111, 4), (1234, 0), (91212129, 9)]
    for sample_input in sample_inputs:
        assert day01.inverse_captcha(sample_input[0]) == sample_input[1]
