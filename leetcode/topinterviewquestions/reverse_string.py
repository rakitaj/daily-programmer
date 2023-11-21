# if (x > 0 && a > INT_MAX - x) // `a + x` would overflow
# if (x < 0 && a < INT_MIN - x) // `a + x` would underflow
#  2,147,483,647
# -2,147,483,648


class Solution:
    int_min = -(2**31)
    int_max = 2**31 - 1

    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            xstring = str(x)[1:]
        else:
            sign = 1
            xstring = str(x)
        result = 0
        for i, c in enumerate(xstring):
            pow_ten = 10 ** (len(xstring) - (len(xstring) - i))
            number = int(c) * pow_ten
            if sign == 1 and result > self.int_max - number:
                return 0
            if sign == -1 and result > (self.int_max + 1) - number:
                return 0
            result += number
        return result * sign
