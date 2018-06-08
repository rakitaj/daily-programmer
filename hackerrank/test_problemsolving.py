from problemsolving import *
import pytest

class TestProblemSolving(object):

    def test_simple_sum_array(self):
        assert simple_sum_array(6, [1, 2, 3, 4, 10, 11]) == 31

    def test_compare_the_triplets(self):
        assert compare_the_triplets((5, 6, 7), (3, 6, 10)) == (1, 1)

    def test_diagonal_difference(self):
        test_data = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
        assert diagonal_difference(test_data) == 15

    def test_plus_minus(self):
        test_data = [-4, 3, -9, 0, 4, 1]
        result = plus_minus(test_data)
        assert round(result[0], 6) == 0.500000
        assert round(result[1], 6) == 0.333333
        assert round(result[2], 6) == 0.166667

    def test_staircase(self):
        expected = "     #\n    ##\n   ###\n  ####\n #####\n######\n"
        assert staircase(6) == expected

    def test_mini_max_sum(self):
        assert mini_max_sum([1, 2, 3, 4, 5]) == (10, 14)

    def test_birthday_cake_candles(self):
        assert birthday_cake_candles([3, 2, 1, 3]) == 2

    def test_time_conversion(self):
        assert time_conversion("12:00:00AM") == "00:00:00"
        assert time_conversion("12:01:01AM") == "00:01:01"
        assert time_conversion("12:35:00AM") == "00:35:00"
        assert time_conversion("01:23:45AM") == "01:23:45"
        assert time_conversion("12:00:00PM") == "12:00:00"
        assert time_conversion("12:30:00PM") == "12:30:00"
        assert time_conversion("07:05:45AM") == "07:05:45"
        assert time_conversion("07:05:45PM") == "19:05:45"

    @pytest.mark.slow    
    def test_time_conversion_thorough(self):
        for half in ["AM", "PM"]:
            for hour in range(1, 13):
                for minute in range(1, 60):
                    for second in range(1, 60):
                        stime = str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(second).zfill(2) + half
                        result = time_conversion(stime)
                        time_tuple = time.strptime(stime, "%I:%M:%S%p")
                        expected = time.strftime("%H:%M:%S", time_tuple)
                        assert result == expected, f"Raw: {stime} Expected: {expected} Actual:{result}"
