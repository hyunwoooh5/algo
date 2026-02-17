class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, best = 0, 0

        for num in nums:
            temp = max(prev + num, best)
            prev, best = best, temp

        return best


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[:2])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        return dp[-1]
