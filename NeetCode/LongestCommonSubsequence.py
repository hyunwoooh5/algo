class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        print(dp)

        return dp[-1][-1]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        memo = [[-1]*n for _ in range(m)]

        def dfs(i, j):
            # out of bound
            if i < 0 or j < 0:
                return 0

            # if there is an obstacle
            if obstacleGrid[i][j] == 1:
                memo[i][j] = 0
                return 0

            # already recorded
            if memo[i][j] != -1:
                return memo[i][j]

            # initial point
            if i == 0 and j == 0:
                memo[i][j] = 1
                return 1

            memo[i][j] = dfs(i-1, j) + dfs(i, j-1)

            return memo[i][j]

        return dfs(m-1, n-1)
