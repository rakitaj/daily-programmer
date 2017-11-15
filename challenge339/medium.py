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

def rental_grid(potential_rental_times):
    grid = [None for i in range(0, len(potential_rental_times))]
    for i in range(0, len(grid)):
        grid[i] = [None for j in range(0, len(potential_rental_times))]
    return grid

def pretty_print_grid(grid):
    for row in grid:
        print(row)

if __name__ == "__main__":
    data = create_rental_tuples("medium_input.txt")
    grid = rental_grid(data)
    pretty_print_grid(grid)
    