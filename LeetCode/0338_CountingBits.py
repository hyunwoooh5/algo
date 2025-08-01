class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []

        for i in range(n+1):
            ans.append(bin(i)[2:].count('1'))
        return ans

# Dynamic Programming
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [0]*(n+1)

        for i in range(1, n+1):
            dp[i] = dp[i//2] + (i % 2)
        return dp
