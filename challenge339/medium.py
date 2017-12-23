from typing import List, Tuple, Sequence
import unittest

def create_rental_tuples(input_data_path) -> List[Tuple[int, int]]:
    """Use known input format to create list of wanted rental times."""
    rental_times = list()
    count = None
    first = None
    second = None
    with open(input_data_path, "r") as text:
        for line_number, line in enumerate(text):
            if line_number == 0:
                count = int(line)
            elif line_number == 1:
                first = line.split()
            elif line_number == 2:
                second = line.split()
    for i in range(0, count):
        rental_times.append((int(first[i]), int(second[i])))
    return rental_times

def by_earliest_end_date(rental_times: List[Tuple[int, int]]) -> Sequence[Tuple[int, int]]:
    result = list()
    while len(rental_times) != 0:
        earliest_end_date = earliest_ending_time(rental_times)
        result.append(earliest_end_date)
        rental_times = remove_overlapping_times(rental_times, earliest_end_date)
    return result

def earliest_ending_time(times: List[Tuple[int, int]]) -> Tuple[int, int]:
    return sorted(times, key=lambda tup: tup[1])[0]

def remove_overlapping_times(all_times, key_time):
    non_overlapping_times = list()
    for time in all_times:
        if time[0] <= key_time[1]:
            pass
        else:
            non_overlapping_times.append(time)
    return non_overlapping_times

def pretty_print_grid(grid):
    for row in grid:
        print(row)

class TimeSchedulingUnitTests(unittest.TestCase):

    def setUp(self):
        self.rental_times = [(1, 23), (10, 12), (5, 10), (12, 29)]
        self.challenge_rental_times = [(1, 23), (10, 12), (5, 10), (12, 29), (13, 25), (40, 66), (30, 35), (22, 33), (70, 100), (19, 65)]

    def test_earliest_end_1(self):
        result = earliest_ending_time(self.rental_times)
        self.assertEqual((5, 10), result)

    def test_remove_overlapping_1(self):
        earliest_end = earliest_ending_time(self.rental_times)
        result = remove_overlapping_times(self.rental_times, earliest_end)
        self.assertListEqual([(12, 29)], result)

if __name__ == "__main__":
    rental_times = create_rental_tuples("medium_input.txt")
    earliest_end_date_solution = by_earliest_end_date(rental_times)
    print(earliest_end_date_solution)
    #unittest.main()
