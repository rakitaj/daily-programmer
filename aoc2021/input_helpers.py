from os.path import abspath, dirname


def puzzle_input_to_str(day: int, strip: bool = False) -> list[str]:
    day_number = str(day).zfill(2)
    dir_name = dirname(__file__)
    file_path = abspath(f"{dir_name}/puzzleinput/day{day_number}.txt")
    with open(file_path, encoding="utf8") as f:
        lines = f.readlines()
    if strip:
        lines = [line.strip() for line in lines]
    return lines


def puzzle_input_to_ints(day: int) -> list[int]:
    day_number = str(day).zfill(2)
    dir_name = dirname(__file__)
    file_path = abspath(f"{dir_name}/puzzleinput/day{day_number}.txt")
    with open(file_path, encoding="utf8") as f:
        lines = f.readlines()
    lines_as_ints = [int(line) for line in lines]
    return lines_as_ints
