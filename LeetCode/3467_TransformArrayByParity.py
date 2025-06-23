class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        e = sum([i % 2 == 0 for i in nums])
        return [0]*e + [1]*(len(nums)-e)
