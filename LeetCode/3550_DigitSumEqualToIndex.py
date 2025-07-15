class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for ind, i in enumerate(nums):
            temp = 0

            while i != 0:
                i, b = i//10, i % 10
                temp += b
            if temp == ind:
                return ind

        return -1
