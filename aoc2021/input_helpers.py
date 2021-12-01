def puzzle_input_to_str(day: int, part: int) -> list[str]:
    day_number = str(day).zfill(2)
    filename = f"day{day_number}-{part}.txt"
    with open(f"./puzzleinput/{filename}") as f:
        lines = f.readlines()
    return lines

def puzzle_input_to_ints(day: int, part: int) -> list[int]:
    day_number = str(day).zfill(2)
    filename = f"day{day_number}-{part}.txt"
    with open(f"./puzzleinput/{filename}") as f:
        lines = f.readlines()
    lines_as_ints = [int(line) for line in lines]
    return lines_as_ints