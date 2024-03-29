class ContainsDuplicate:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_seen: set[int] = set()
        for num in nums:
            if num in nums_seen:
                return True
            nums_seen.add(num)
        return False


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
        move_to = 0
        for num in nums:
            if num != 0:
                nums[move_to] = num
                move_to += 1
        for i in range(move_to, len(nums)):
            nums[i] = 0


class RemoveDuplicates:
    def remove_dupes(self, nums: list[int]) -> int:
        """
        Remove duplicates from an already sorted array.
        Input: nums = [0,0,1,1,1,2,2,3,3,4]
        Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
        """
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k


class StockProfits:
    def max_profit(self, prices: list[int]) -> int:
        """
        Input: [7, 1, 5, 3, 6, 4]
        Max profit: 7
        """
        profit = 0
        prev_i = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                profit += prices[i - 1] - prices[prev_i]
                prev_i = i
        if (prices[-1] - prices[prev_i]) > 0:
            profit += prices[-1] - prices[prev_i]
        return profit

    def max_profit_simple(self, prices: list[int]) -> int:
        """
        Input: [7, 1, 5, 3, 6, 4]
        Max profit: 7
        """
        profit = 0
        for i in range(1, len(prices)):
            p = prices[i] - prices[i - 1]
            if p > 0:
                profit += p
        return profit
