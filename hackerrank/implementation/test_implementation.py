from hackerrank.implementation.implementation import *
from hackerrank.implementation.bonappetit import bon_appetit
import pytest

class TestImplementation(object):

    def test_grading(self):
        assert grading([73, 67, 38, 33]) == [75, 67, 40, 33]
        assert grading([37, 0, 100, 99, 98, 97]) == [37, 0, 100, 100, 100, 97]

    def test_kangaroo(self):
        assert kangaroo(0, 3, 4, 2) == "YES"
        assert kangaroo(0, 2, 5, 3) == "NO"
        
    def test_apple_and_orange(self):
        assert apple_and_orange(7, 11, 5, 15, [-2, 2, 1], [5, -6]) == (1, 1)

    def test_between_two_sets(self):
        assert between_two_sets([2, 4], [16, 32, 96]) == [4, 8, 16]

    def test_breaking_the_records(self):
        assert breaking_the_records([10, 5, 20, 20, 4, 5, 2, 25, 1]) == (2, 4)

    def test_the_birthday_bar(self):
        assert the_birthday_bar([1, 2, 1, 3, 2], 3, 2) == 2
        assert the_birthday_bar([1, 1, 1, 1, 1, 1], 3, 2) == 0
        assert the_birthday_bar([4], 4, 1) == 1

    def test_divisible_sum_pairs(self):
        assert divisible_sum_pairs(6, 3, [1, 3, 2, 6, 1, 2]) == 5


    def test_migratory_birds(self):
        assert migratory_birds([1, 4, 4, 4, 5, 3]) == 4

    def test_day_of_the_programmer(self):
        assert day_of_the_programmer(1800) == "12.09.1800"
        assert day_of_the_programmer(1918) == "26.09.1918"
        assert day_of_the_programmer(2016) == "12.09.2016"
        assert day_of_the_programmer(2017) == "13.09.2017"

    def test_is_leap_year(self):
        assert is_leap_year(1918) is False
        assert is_leap_year(1996) is True
        assert is_leap_year(1997) is False
        assert is_leap_year(2000) is True
        assert is_leap_year(2004) is True
        assert is_leap_year(1900) is True # Uses Julian calendar pre 1917
        assert is_leap_year(2100) is False
        assert is_leap_year(2200) is False
        assert is_leap_year(2400) is True

    def test_sock_monstor(self):
        assert sock_monster([10, 20, 20, 10, 10, 30, 50, 10, 20]) == 3

    @pytest.mark.parametrize("length, page, expected", [
        (5, 4, 0),
        (4, 4, 0),
        (4, 1, 0),
        (6, 1, 0),(6, 2, 1),(6, 3, 1),(6, 4, 1),(6, 5, 1),(6, 6, 0),
        (9, 1, 0),(9, 2, 1),(9, 3, 1),(9, 4, 2),(9, 5, 2),(9, 6, 1),(9, 7, 1),(9, 8, 0),(9, 9, 0)
    ])
    def test_drawing_book(self, length, page, expected):
        assert drawing_book(length, page) == expected

    def test_counting_valleys(self):
        sample_data = "UDDDUDUU"
        assert counting_valleys(len(sample_data), sample_data) == 1

    def test_electronics_shop(self):
        assert electronics_shop([3, 1], [5, 2, 8], 10) == 9
        assert electronics_shop([4], [5], 5) == -1

    def test_cats_and_a_mouse(self):
        assert cats_and_a_mouse(1, 2, 3) == "Cat B"
        assert cats_and_a_mouse(1, 3, 2) == "Mouse C"

    def test_picking_numbers(self):
        assert picking_numbers([4, 6, 5, 3, 3, 1]) == 3
        assert picking_numbers([1, 2, 2, 3, 1, 2]) == 5

    def test_climbing_the_leaderboard(self):
        assert climbing_the_leaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]) == [6, 4, 2, 1]
        print(climbing_the_leaderboard([97, 93, 88, 29, 2], [34, 74, 79]))

    #def test_get_standing(self):
    #    assert get_standing([100, 100, 50, 40, 40, 20, 10], 50) == 2

def test_bon_appetit():
    assert bon_appetit(1, [3, 10, 2, 9], 12) == 5
    assert bon_appetit(1, [3, 10, 2, 9], 7) == "Bon Appetit"
