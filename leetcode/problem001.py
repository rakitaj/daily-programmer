from typing import Tuple, List, Dict


class Solution:

    def two_sum(self, nums: List[int], target: int) -> Tuple[int, int]:
        values_seen: Dict[int, int] = {}
        for i, value in enumerate(nums, 1):
            if value in values_seen:
                result = (values_seen[value], i)
                break
            else:
                values_seen[target - value] = i
        return result
