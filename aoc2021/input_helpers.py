from enum import Enum
from os.path import abspath, dirname


class DataType(Enum):
    REGULAR = 0
    TEST = 1


def puzzle_input_to_str(day: int, strip: bool = False) -> list[str]:
    day_number = str(day).zfill(2)
    filename = f"day{day_number}.txt"
    dir_name = dirname(__file__)
    filepath = abspath(f"{dir_name}/puzzleinput/{filename}")
    return _filename_to_str(filepath, strip)


def _filename_to_str(filepath: str, strip: bool) -> list[str]:
    with open(filepath, encoding="utf8") as f:
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


def file_loader(filename: str, datatype: DataType = DataType.REGULAR, strip: bool = False) -> list[str]:
    dir_name = dirname(__file__)
    if datatype == DataType.REGULAR:
        filepath = abspath(f"{dir_name}/puzzleinput/{filename}")
    else:
        filepath = abspath(f"{dir_name}/testdata/{filename}")
    result = _filename_to_str(filepath, strip)
    return result
