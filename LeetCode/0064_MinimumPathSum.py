class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        dp = [[0 for i in range(cols)] for j in range(rows)]
        dp[0][0] = grid[0][0]

        for i in range(1, rows):
            dp[i][0] = dp[i-1][0]+grid[i][0]

        for j in range(1, cols):
            dp[0][j] = dp[0][j-1]+grid[0][j]

        for i in range(rows):
            for j in range(cols):
                if i != 0 and j != 0:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        return dp[rows-1][cols-1]
