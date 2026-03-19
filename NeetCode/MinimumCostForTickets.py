class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = days[-1]

        dp = [0]*(n+1)

        for i in range(1, n+1):
            if i in days:
                dp[i] = min(dp[i-1] + costs[0], dp[max(0, i-7)] +
                            costs[1], dp[max(0, i-30)] + costs[2])
            else:
                dp[i] = dp[i-1]

        return dp[-1]


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}

        n = len(days)

        def dfs(i):
            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = float("inf")

            j = i

            for d, c in zip([1, 7, 30], costs):
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                memo[i] = min(memo[i],  c + dfs(j))

            return memo[i]

        return dfs(0)
