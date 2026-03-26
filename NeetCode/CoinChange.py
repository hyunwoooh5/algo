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


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]

            res = 1e10

            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))

            memo[amount] = res

            return res

        res = dfs(amount)

        return -1 if res == 1e10 else res


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount+1]*(amount+1)

        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)

        if dp[-1] == amount+1:
            return -1
        return dp[-1]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]

            res = 1e10

            for coin in coins:
                if amount >= coin:
                    res = min(res, 1+dfs(amount-coin))

            memo[amount] = res

            return res

        ans = dfs(amount)

        return ans if ans != 1e10 else -1
