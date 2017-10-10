import json
import unittest
import sys

def create_list_of_peaks_From_json(path, name):
    with open(path, "r") as json_data:
        data = json.load(json_data)
        numbers = data[name].split()
        numbers_as_ints = [int(i) for i in numbers]
        return numbers_as_ints

def calculate_summit_order(peaks):
    first = peaks[0]
    peaks = peaks[1:]
    return build_summit_order(peaks, [first])

def calculate_summit_order_dynamic(peaks):
    summits = [[n] for n in peaks]
    for j in range(1, len(peaks)):
        for i in range(j):
            if peaks[j] > peaks[i] and len(summits[j]) < len(summits[i]) + 1:
                summits[j] = summits[i] + [peaks[j]]
    return max(summits, key=len)

def build_summit_order(peaks, summits):
    if len(peaks) == 0:
        return summits
    else:
        last_summit = summits[len(summits) - 1]
        result = find_next_biggest_number(last_summit, peaks)
        if result.number != None:
            summits.append(result.number)
        return build_summit_order(peaks[result.index + 1:], summits)
    
def find_next_biggest_number(current_number, numbers):
    smallest_diff_index = 0
    smallest_diff = find_max_diff(current_number, numbers)
    for index, item in enumerate(numbers):
        diff = item - current_number
        if diff == 1:
            return NumberAndIndex(index, item)
        elif diff > 0 and diff < smallest_diff:
            smallest_diff = diff
            smallest_diff_index = index
        else:
            pass
    if smallest_diff_index == 0:
        return NumberAndIndex(0, None)
    return NumberAndIndex(smallest_diff_index, numbers[smallest_diff_index])

def find_max_diff(current_number, numbers):
    max_diff = 0
    for n in numbers:
        if n - current_number > max_diff:
            max_diff = n -current_number
    return max_diff

class NumberAndIndex:

    def __init__(self, index, number):
        self.index = index
        self.number = number

class SummitTests(unittest.TestCase):

    def test_find_next_biggest_number_1(self):
        numbers = [1, 6, 4, 7, 9 , 8, 10]
        result = find_next_biggest_number(1, numbers)
        self.assertEqual(result.index, 2)
        self.assertEqual(result.number, 4)

    def test_find_max_diff_1(self):
        numbers = [3, 9, 4]
        result = find_max_diff(2, numbers)
        self.assertEqual(result, 7)

    def test_find_max_diff_2(self):
        numbers = [21]
        result = find_max_diff(21, numbers)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
        data_name = sys.argv[2]
        peaks = create_list_of_peaks_From_json(path, data_name)
        #result = calculate_summit_order(peaks)
        result = calculate_summit_order_dynamic(peaks)
        print(result)
    else:
        unittest.main(argv=None)