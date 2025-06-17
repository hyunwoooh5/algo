class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, best = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if best < ans:
                    best = ans
                ans = 0
            else:
                ans += 1

        return ans if best < ans else best
