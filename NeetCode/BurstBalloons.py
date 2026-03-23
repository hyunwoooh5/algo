class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        n = len(nums)

        dp = [[0]*n for _ in range(n)]

        for length in range(1, n-1):
            for i in range(n-length-1):  # left
                j = i + length + 1  # right

                for k in range(i+1, j):
                    coins = nums[i] * nums[k] * nums[j]

                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + coins)

        return dp[0][n-1]


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        memo = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]

            memo[(l, r)] = 0

            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dfs(l, i-1) + dfs(i+1, r)

                memo[(l, r)] = max(memo[(l, r)], coins)

            return memo[(l, r)]

        return dfs(1, len(nums)-2)
