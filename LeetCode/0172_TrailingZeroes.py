class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(1, n+1):
            while i >= 5:
                i, r = i//5, i % 5
                if r == 0:
                    ans += 1
                else:
                    break

        return ans
