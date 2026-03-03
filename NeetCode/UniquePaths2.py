class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[-1]*n for _ in range(m)]

        def dfs(i, j):
            if i >= m or j >= n:
                return 0

            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
                return 0

            if i == m-1 and j == n-1:
                return 1

            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = dfs(i, j+1) + dfs(i+1, j)

            return dp[i][j]

        return dfs(0, 0)


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i-1][j] == 1 and obstacleGrid[i][j-1] == 1:
                    dp[i][j] = 0
                elif obstacleGrid[i-1][j] == 1:
                    dp[i][j] = dp[i][j-1]
                elif obstacleGrid[i][j-1] == 1:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

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
