def sliding_window(nums: list[int], start: int, lookback: int) -> float:
    total = 0
    for i in range(start - (lookback - 1), start + 1):
        total += nums[i]
    return total