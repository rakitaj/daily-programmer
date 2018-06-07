from implementation import *

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