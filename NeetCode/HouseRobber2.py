class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev, best = 0, 0

        for num in nums[:-1]:
            temp = max(prev+num, best)
            prev, best = best, temp

        ans = best

        prev, best = 0, 0

        for num in nums[1:]:
            temp = max(prev+num, best)
            prev, best = best, temp

        return max(ans, best)
