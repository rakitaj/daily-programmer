"""Leetcode explore array module.
Searching for items in an array."""


def check_if_n_and_double_exists(arr: list[int]) -> bool:
    """Check If N and Its Double Exist."""
    seen: set[int] = set()
    for i in arr:
        if i * 2 in seen or i / 2 in seen:
            return True
        seen.add(i)
    return False


def valid_mountain_array(arr: list[int]) -> bool:
    """Valid Mountain Array."""
    if len(arr) < 3:
        return False
    went_up = False
    summited = False
    for i in range(len(arr) - 1):
        if summited:
            if arr[i] <= arr[i + 1]:
                return False
        else:
            if arr[i + 1] < arr[i]:
                summited = True
            elif arr[i] == arr[i + 1]:
                return False
            else:
                went_up = True
    return went_up and summited
