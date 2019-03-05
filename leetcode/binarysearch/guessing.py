"""LeetCode guessing game."""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):


def guess(n: int) -> int:
    if n == Solution.TARGET_NUMBER:
        return 0
    elif n > Solution.TARGET_NUMBER:
        return -1
    else:
        return 1

class Solution(object):

    TARGET_NUMBER = 0

    def guessNumber(self, n: int) -> int:
        low = 0
        high = n
        my_guess = (low + high) // 2
        guess_result = guess(my_guess)
        while guess_result != 0:
            if guess_result == -1:
                high = my_guess - 1
            else:
                low = my_guess + 1
            my_guess = (low + high) // 2
            guess_result = guess(my_guess)
        return int(my_guess)
