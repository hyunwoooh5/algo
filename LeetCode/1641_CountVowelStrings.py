class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0, 0, 0, 0, 0] for _ in range(n+1)]
        dp[0] = [0, 0, 0, 0, 0]
        dp[1] = [1, 1, 1, 1, 1]

        for i in range(2, n+1):
            for j in range(5):
                for k in range(j+1):
                    dp[i][j] += dp[i-1][k]

        return sum(dp[-1])
