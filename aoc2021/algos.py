def sliding_window(nums: list[int], start: int, lookback: int) -> int:
    total = 0
    for i in range(start - (lookback - 1), start + 1):
        total += nums[i]
    return total


def bits_to_decimal(bits: list[int]) -> int:
    """Pass the bits least significant bit first. Aka in the 0th index."""
    total = 0
    for i in range(len(bits)):
        if bits[i] == 1:
            total += pow(2, i)
    return total
