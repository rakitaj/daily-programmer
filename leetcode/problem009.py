class Solution:

    def is_palindrome(self, number: int) -> bool:
        """Returns whether the input number is a palindromic number."""
        if number < 0:
            return False
        else:
            string_number = str(number)
            start = 0
            end = len(string_number) - 1
            while start <= end:
                if string_number[start] == string_number[end]:
                    start += 1
                    end -= 1
                else:
                    return False
        return True

    isPalindrome = is_palindrome
