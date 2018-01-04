import pytest
import day01, day02, day03, day04, day05, day06, day07

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

@pytest.mark.parametrize("input, expected", [
    ("aa bb cc dd ee", True),
    ("aa bb cc dd aa", False),
    ("aa bb cc dd aaa", True)
])
def test_day04_is_passphrase_valid(input, expected):
    assert day04.basic_validation(input) == expected

@pytest.mark.parametrize("input, expected", [
    ("abcde fghij", True),
    ("abcde xyz ecdab", False),
    ("a ab abc abd abf abj", True),
    ("iiii oiii ooii oooi oooo", True),
    ("oiii ioii iioi iiio", False)
])
def test_day04_is_passphrase_valid_with_no_anagrams(input, expected):
    assert day04.anagram_validation(input) == expected

def test_day05_part1():
    sample_input = [0, 3, 0, 1, -3]
    assert day05.escape(sample_input, day05.part_one) == 5

def test_day05_part2():
    sample_input = [0, 3, 0, 1, -3]
    assert day05.escape(sample_input, day05.part_two) == 10

def test_day06_part1():
    sample_input = [0, 2, 7, 0]
    assert day06.memory_cycles(sample_input).count == 5

def test_day06_part2():
    sample_input = [0, 2, 7, 0]
    assert day06.memory_cycles(sample_input).previous_dupe == 4

def test_day07_create_with_children():
    text = "fwft (72) -> ktlj, cntj, xhth"
    expected = day07.Node("fwft", 72, ("ktlj", "cntj", "xhth"))
    assert day07.Node.create(text) == expected

def test_day07_create_without_children():
    text = "ktlj (57)"
    expected = day07.Node("ktlj", 57)
    assert day07.Node.create(text) == expected