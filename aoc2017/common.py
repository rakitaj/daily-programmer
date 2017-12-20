"""
Common functions I will use often during Advent Of Code 2017.
"""

def number_from_text_file(path: str) -> int:
    with open(path, "r") as file:
        number_string = file.read()
        return int(number_string)
