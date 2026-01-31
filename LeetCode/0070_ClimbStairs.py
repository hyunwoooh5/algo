class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2

        a, b = 1, 2

        # Fibonacci without calling function
        for _ in range(3, n+1):
            a, b = b, a+b

        return b


# Dynamic Programming
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        dp[0] = 1

        for i in range(1, n+1):
            for k in 1, 2:
                if i >= k:
                    dp[i] += dp[i-k]

        return dp[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1

        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]

        return dp[-1]
