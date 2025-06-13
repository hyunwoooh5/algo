class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(range(1, len(nums)+1))
        l = set(nums)
        return list(s-l)
