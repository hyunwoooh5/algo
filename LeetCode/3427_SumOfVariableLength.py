class Solution(object):
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0

        for ind, i in enumerate(nums):
            ans += sum(nums[max(0, ind-i):ind+1])
        return ans