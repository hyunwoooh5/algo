class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        current = sum(nums[:k])
        ans = current
        for i in range(k, len(nums)):
            current = current - nums[i-k]+nums[i]
            ans = max(ans, current)
        return float(ans)/k
