from typing import List, Tuple
from common import true_for_all

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
        set_1_is_factor = true_for_all(set_1, (lambda item, i=i: i % item == 0))
        is_factor_for_set_2 = true_for_all(set_2, (lambda item, i=i: item % i == 0))
        if set_1_is_factor and is_factor_for_set_2:
            result.append(i)
    return result

def breaking_the_records(scores: List[int]) -> Tuple[int, int]:
    min_score = scores[0]
    max_score = scores[0]
    min_score_count = 0
    max_score_count = 0
    for score in scores:
        if score > max_score:
            max_score = score
            max_score_count += 1
        if score < min_score:
            min_score = score
            min_score_count += 1
    return (max_score_count, min_score_count)

def the_birthday_bar(numbers, day, month) -> int:
    