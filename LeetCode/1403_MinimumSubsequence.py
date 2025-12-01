class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        nums.append(0)

        for i in range(len(nums)):
            if sum(nums[:i]) > sum(nums[i:]):
                return nums[:i]
