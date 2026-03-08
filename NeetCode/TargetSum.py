class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)

        if abs(s) > s or (s+target) % 2 == 1:
            return 0

        new_target = (s+target)//2

        dp = [0]*(new_target+1)
        dp[0] = 1

        for num in nums:
            for i in range(new_target, num-1, -1):
                dp[i] += dp[i-num]

        return dp[-1]


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, cur_sum):
            if i == len(nums):
                return 1 if cur_sum == target else 0

            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]

            add = dfs(i+1, cur_sum + nums[i])
            subtract = dfs(i+1, cur_sum - nums[i])

            memo[(i, cur_sum)] = add + subtract

            return memo[(i, cur_sum)]

        return dfs(0, 0)
