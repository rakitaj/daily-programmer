from typing import List, Tuple, Dict
from common import true_for_all, sum_desired_length

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

def the_birthday_bar(numbers: List[int], day: int, month: int) -> int:
    desired_length = month
    desired_sum = day
    solution_count = 0
    print(len(numbers) - desired_length)
    for i in range(len(numbers) - desired_length + 1):
        if sum_desired_length(numbers, i, desired_length) == desired_sum:
            solution_count += 1
    return solution_count

def divisible_sum_pairs(n: int, k: int, array: List[int]) -> int:
    valid_pairs: List[Tuple[int, int]] = list()
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if (array[i] + array[j]) % k == 0:
                valid_pairs.append((array[i], array[j]))
    print(valid_pairs)
    return len(valid_pairs)

def migratory_birds(array: List[int]) -> int:
    numbers_count: Dict[int, int] = dict()
    for number in array:
        if number in numbers_count:
            numbers_count[number] += 1
        else:
            numbers_count[number] = 1
    return max(numbers_count, key=numbers_count.get)
    
def day_of_the_programmer(year: int) -> str:
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = 256
    if is_leap_year(year):
        months[2] = 29
    if year == 1918:
        months[2] = 15
    for month, days_in_month in enumerate(months):
        if days_in_month > count:
            return "{0}.{1}.{2}".format(str(count).zfill(2), str(month).zfill(2), year)
        else:
            count -= days_in_month

def is_leap_year(year: int) -> bool:
    if year <= 1917:
        return year % 4 == 0
    else:
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
