class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if len(s) == 0:
            return 0

        digits = [str(i) for i in range(10)]

        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] in digits:
            sign = 1
        elif s[0] == "+":
            sign = 1
            s = s[1:]
        else:
            return 0

        result = '0'
        for i in range(len(s)):
            if s[i] in digits:
                result += s[i]
            else:
                break

        result = sign*int(result)

        if result > 2**31-1:
            return 2**31-1
        elif result < -2**31:
            return -2**31
        else:
            return result
