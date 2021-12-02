def puzzle_input_to_str(day: int) -> list[str]:
    day_number = str(day).zfill(2)
    with open(f"./puzzleinput/day{day_number}.txt") as f:
        lines = f.readlines()
    return lines


def puzzle_input_to_ints(day: int) -> list[int]:
    day_number = str(day).zfill(2)
    with open(f"./puzzleinput/day{day_number}.txt") as f:
        lines = f.readlines()
    lines_as_ints = [int(line) for line in lines]
    return lines_as_ints
