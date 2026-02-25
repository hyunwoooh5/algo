class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [2*amount+0.1]*(amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i-c >= 0:
                    dp[i] = min(dp[i], dp[i-c]+1)

        if dp[-1] == 2*amount+0.1:
            return -1
        return dp[-1]
