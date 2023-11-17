# if (x > 0 && a > INT_MAX - x) // `a + x` would overflow
# if (x < 0 && a < INT_MIN - x) // `a + x` would underflow


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
            if sign == 1 and result > self.int_max - int(c):
                return 0
            if sign == -1 and result > (self.int_max + 1) - int(c):
                return 0
            pow_ten = 10 ** (len(xstring) - (len(xstring) - i))
            result += int(c) * pow_ten
        return result * sign
