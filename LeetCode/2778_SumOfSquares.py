class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        n = len(nums)
        for ind, num in enumerate(nums):
            if n % (ind+1) == 0:
                ans += num**2
        return ans
