import pytest
import day01
import day02
import day03

@pytest.mark.parametrize("sample_input,expected", [
    (1122, 3), (1111, 4), (1234, 0), (91212129, 9)
])
def test_day01_part1(sample_input, expected):
    assert day01.inverse_captcha(1, sample_input) == expected

@pytest.mark.parametrize("sample_input,expected", [
    (1212, 6), (1221, 0), (123425, 4), (123123, 12), (12131415, 4)
])
def test_day01_part2(sample_input, expected):
    amount = int(len(str(sample_input)) / 2)
    assert day01.inverse_captcha(amount, sample_input) == expected

def test_day02_part1():
    sample_data = [(5, 1, 9, 5), (7, 5, 3), (2, 4, 6, 8)]
    actual = day02.checksum(sample_data, day02.diff_checksum)
    assert actual == 18

def test_day02_part2():
    sample_data = [(5, 9, 2, 8), (9, 4, 7, 3), (3, 8, 6, 5)]
    actual = day02.checksum(sample_data, day02.div_checksum)
    assert actual == 9

def test_day03_generate_spiral_sequence():
    result = list()
    for i in day03.generate_spiral_sequence(8):
        result.append(i)
    assert result == [1, 1, 2, 2, 3, 3, 4, 4]