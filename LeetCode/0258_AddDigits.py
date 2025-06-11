class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)

        if len(num) == 1:
            return int(num)

        while len(num) != 1:
            ans = 0
            for i in range(len(num)):
                ans += int(num[i])
            num = str(ans)

        return ans
