class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)

        target = total_sum // 2

        dp = [0]*(target+1)

        for stone in stones:
            for i in range(target, stone-1, -1):
                dp[i] = max(dp[i], dp[i-stone] + stone)

        return total_sum - 2*dp[-1]


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)

        target = total_sum // 2

        dp = {}

        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (total_sum - total))

            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = min(dfs(i+1, total), dfs(i+1, total+stones[i]))

            return dp[(i, total)]

        return dfs(0, 0)
