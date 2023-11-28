class ContainsDuplicate:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_seen: set[int] = set()
        for num in nums:
            if num in nums_seen:
                return True
            nums_seen.add(num)
        return False


class MaxProfit:
    def maxProfit(self, prices: list[int]) -> int:
        i = 0
        total = 0
        while i < len(prices):
            for j in range(i, len(prices)):
                if prices[j] > prices[i]:
                    pass
        return total


class ArrayPlusOne:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9 and i == 0:
                digits[i] = 0
                digits.insert(0, 1)
                # Done after this no need to break
            elif digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
        return digits

    def plus_one_v2(self, digits: list[int]) -> list[int]:
        """Take advantage of the no leading 0s rule."""
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
        if digits[0] == 0:
            digits.insert(0, 1)
            # Done after this no need to break
        return digits


class MoveZeros:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        offset = 0
        i = 0
        while i < len(nums) - offset:
            if nums[i] == 0:
                # Bubble forwards
                self._bubble_forwards(nums, i, len(nums) - offset)
                offset += 1
                continue
            i += 1

    def _bubble_forwards(self, nums: list[int], target_i: int, end: int) -> None:
        for i in range(target_i, end - 1):
            temp = nums[i + 1]
            nums[i + 1] = nums[i]
            nums[i] = temp

    def move_zeroes_v2(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
        for i, e in enumerate(nums):
            if e == 0:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
