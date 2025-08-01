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
