class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = 1
        for i in range(1, m):
            ans /= i
        for i in range(1, n):
            ans /= i
        for i in range(1, m+n-1):
            ans *= i

        return int(ans+0.9)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if i == m-1 and j == n-1:
                return 1
            if i >= m or j >= n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = dfs(i, j+1) + dfs(i+1, j)

            return dp[i][j]

        return dfs(0, 0)
