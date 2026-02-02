class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums)+1)
        dp[1] = nums[0]
        for i, num in enumerate(nums[1:]):
            dp[i+2] = max(dp[i]+num, dp[i+1])

        return dp[-1]


# Space optimization
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, best = 0, 0

        for num in nums:
            temp = max(best, prev+num)
            prev, best = best, temp

        return best
