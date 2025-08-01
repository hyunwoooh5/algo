class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = [[0 for i in range(j)] for j in range(1, n+1)]

        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i-1][j]
                elif j == i:
                    dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])
            # print(dp)
        return min(dp[-1])
