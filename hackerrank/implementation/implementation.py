from typing import List, Tuple, Dict
from math import floor, ceil
from hackerrank.common import true_for_all, sum_desired_length, dedupe_sequence, numbers_to_counts
import bisect

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
    numbers_count = numbers_to_counts(array)
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
            result = "{0}.{1}.{2}".format(str(count).zfill(2), str(month).zfill(2), year)
            break
        else:
            count -= days_in_month
    return result

def is_leap_year(year: int) -> bool:
    if year <= 1917:
        return year % 4 == 0
    else:
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def sock_monster(socks: List[int]) -> int:
    sock_count = numbers_to_counts(socks)
    pairs_of_socks = 0
    for key, value in sock_count.items():
        pairs_of_socks += floor(value / 2)
    return pairs_of_socks

def drawing_book(book_length: int, page: int) -> int:
    turns = floor(page / 2)
    half_book = floor(book_length / 2)
    forwards = turns
    backwards = half_book - turns
    return min(forwards, backwards)

def counting_valleys(n: int, s: List[int]) -> int:
    valleys_count = 0
    counter = 0
    for step in s:
        if step == "U":
            counter += 1
        elif step == "D":
            counter -= 1
        else:
            raise ValueError("Step has to have value of U or D.")
        if counter == 0:
            if step == "U":
                valleys_count += 1
    return valleys_count

def electronics_shop(keyboards: List[int], drives: List[int], b: int) -> int:
    spend = -1
    for keyboard in keyboards:
        for drive in drives:
            if (keyboard + drive) > spend and (keyboard + drive) <= b:
                spend = keyboard + drive
    return spend

def cats_and_a_mouse(x: int, y: int, z: int) -> str:
    x_diff = abs(z - x)
    y_diff = abs(z - y)
    if x_diff == y_diff:
        return "Mouse C"
    elif x_diff < y_diff:
        return "Cat A"
    else:
        return "Cat B"

def picking_numbers(numbers: List[int]) -> int:
    numbers = sorted(numbers)
    max_length, length = 0, 0
    for i, n_i in enumerate(numbers):
        length = 0
        for j, n_j in enumerate(numbers, i):
            diff = n_j - n_i
            if diff == 0 or diff == 1:
                length += 1
        if length > max_length:
            max_length = length
    return max_length

def climbing_the_leaderboard(scores: List[int], alice: List[int]) -> List[int]:
    # [100, 50, 52, 20] - [5, 25, 50, 125]
    uniques: List[int] = dedupe_sequence(scores)
    length = len(uniques)
    alice_standings = list()
    for alice_score in alice:
        while (length > 0) and (alice_score >= uniques[length-1]):
            length -= 1
        alice_standings.append(length + 1)
    return alice_standings

def get_standing(highscores: List[int], new_score: int) -> int:
    low = 0
    high = len(highscores) - 1
    while low < high:
        middle = floor((low+high)/2)
        if new_score == highscores[middle]:
            break
        elif new_score > highscores[middle]:
            low = middle
        elif new_score < highscores[middle]:
            high = middle
        elif low == high:
            middle = low
            break
    return middle + 1

def the_hurdle_race(jump_height: int, hurdles: List[int]) -> int:
    max_height = max(hurdles)
    height_diff = max_height - jump_height
    if height_diff > 0:
        return height_diff
    else:
        return 0

def designer_pdf_viewer(letters: List[str], word: str) -> int:
    heights = list()
    for letter in word:
        index = ord(letter) - 97
        heights.append(int(letters[index]))
    max_height = max(heights)
    return len(word) * max_height

def utopian_tree(n: int) -> int:
    height = 1
    for i in range(1, n+1):
        if i % 2 == 0:
            height += 1
        else:
            height = height * 2
    return height

def angry_professor(k: int, a: List[int]) -> str:
    on_time_count = 0
    for arrival_time in a:
        if arrival_time <= 0:
            on_time_count += 1
    if on_time_count >= k:
        return "NO"
    else:
        return "YES"

def big_sorting(number_strings: List[str]) -> List[int]:
    numbers = [int(string) for string in number_strings]
    sorted_numbers = sorted(numbers)
    return sorted_numbers
