class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev, best1 = 0, 0

        for num in nums[:-1]:
            temp = max(best1, prev+num)
            prev, best1 = best1, temp

        prev, best2 = 0, 0
        for num in nums[1:]:
            temp = max(best2, prev+num)
            prev, best2 = best2, temp

        return max(best1, best2)
