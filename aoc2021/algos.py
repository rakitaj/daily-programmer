"""Common classes and algorithms for Advent of Code 2021."""


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Point):
            return self.x == __o.x and self.y == __o.y
        else:
            return False

    def __str__(self) -> str:
        return f"(x:{self.x}, y:{self.y})"

    def __repr__(self) -> str:
        return str(self)


def sliding_window(nums: list[int], start: int, lookback: int) -> int:
    total = 0
    for i in range(start - (lookback - 1), start + 1):
        total += nums[i]
    return total


def bits_to_decimal(bits: list[int], endianness: str) -> int:
    """Pass the bits least significant bit first. Aka in the 0th index."""
    total = 0
    length = len(bits)
    if endianness == "little":
        for i in range(length):
            if bits[i] == 1:
                total += pow(2, i)
    elif endianness == "big":
        # Using what looks like funky start stop because I need to hit the 0th element.
        for i in range(length - 1, -1, -1):
            if bits[i] == 1:
                total += pow(2, (length - 1) - i)
    else:
        raise ValueError(f"Endianness must be little or big. Value of {endianness} is not known.")
    return total


def most_common_bit(bits_list: list[str], i: int) -> int:
    total = 0
    for bits in bits_list:
        total += int(bits[i])
    return round(total / len(bits_list))


def count_bits(bits_list: list[str], i: int) -> tuple[int, int]:
    """Count the bits in the given position for the list of bits.
    Return a tuple in the form of (count of 0s, count of 1s)"""
    count0s = 0
    count1s = 0
    for bits in bits_list:
        if bits[i] == "0":
            count0s += 1
        elif bits[i] == "1":
            count1s += 1
        else:
            raise ValueError(f"Bit value in {bits} at position {i} is not valid.")
    return (count0s, count1s)
