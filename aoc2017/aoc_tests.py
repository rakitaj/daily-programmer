import pytest
import day01

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
    