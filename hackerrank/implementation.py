from typing import List, Tuple

def grading(raw_grades: List[int]) -> List[int]:
    rounded_grades = list()
    for grade in raw_grades:
        if grade <= 37:
            rounded_grades.append(grade)
        else:
            if grade % 5 >= 3:
                rounded = grade + (5 - (grade % 5))
                rounded_grades.append(rounded)
            else:
                rounded_grades.append(grade)
    return rounded_grades

def kangaroo(x1: int, v1: int, x2: int, v2: int) -> str:
    if x1 == x2 and v1 == v2:
        return "YES"
    elif x1 != x2 and v1 == v2:
        return "NO"
    else:
        result = (x2 - x1) / (v1 - v2)
        if result % 1 == 0 and result > 0:
            return "YES"
        else:
            return "NO"

def apple_and_orange(s: int, t: int, a: int, b: int, apples: List[int], oranges: List[int]) -> Tuple[int, int]:
    apple_hit_count = 0
    orange_hit_count = 0
    for apple_distance in apples:
        if s <= a + apple_distance <= t:
            apple_hit_count += 1
    for orange_distance in oranges:
        if s <= b + orange_distance <= t:
            orange_hit_count += 1
    return (apple_hit_count, orange_hit_count)

def between_two_sets(set_1: List[int], set_2: List[int]) -> List[int]:
    all_items = set_1 + set_2
    minimum = min(all_items)
    maximum = max(all_items)
    result: List[int] = list()
    for i in range(minimum, maximum + 1):
        set_1_is_factor = true_for_all_items(set_1, (lambda item, i=i: i % item == 0))
        is_factor_for_set_2 = true_for_all_items(set_2, (lambda item, i=i: item % i == 0))
        if set_1_is_factor and is_factor_for_set_2:
            result.append(i)
    return result

def true_for_all_items(items: List, func) -> bool:
    for item in items:
        result = func(item)
        if result is not True:
            return False
    return True

class TestImplementation(object):

    def test_true_for_all_items_should_be_true(self):
        items = [2, 4, 6, 8, 12, 16, 24]
        truth_func = lambda x: x % 2 == 0
        assert true_for_all_items(items, truth_func) is True

    def test_true_for_all_items_with_bad_data_should_be_false(self):
        items = [2, 4, 6, 8, 13, 16, 24]
        truth_func = lambda x: x % 2 == 0
        assert true_for_all_items(items, truth_func) is False

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