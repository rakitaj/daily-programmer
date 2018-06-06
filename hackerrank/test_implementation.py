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
