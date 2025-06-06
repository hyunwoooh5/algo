class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        sign = 1
        if x[0] == '-':
            sign = -1
            x = x[1:]

        ans = sign*int(x[::-1])

        if ans < -2**31 or ans > 2**31-1:
            return 0
        return ans
