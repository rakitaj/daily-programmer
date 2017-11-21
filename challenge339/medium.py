from typing import List, Tuple

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

def all_possibilities(times):
    grid = list()
    for time in times:
        grid.append(calculate_row(time, times))
    return grid

def calculate_row(first_time, times):
    rental_list = list()
    rental_list.append(first_time)
    for time in times:
        if time[0] > rental_list[-1][1]:
            rental_list.append(time)
    return rental_list

def pretty_print_grid(grid):
    for row in grid:
        print(row)

if __name__ == "__main__":
    rental_times = create_rental_tuples("medium_input.txt")
    sorted_times = sorted(rental_times, key=lambda tup: tup[0])
    grid = all_possibilities(sorted_times)
    pretty_print_grid(grid)
    