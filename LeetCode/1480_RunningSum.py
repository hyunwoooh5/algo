class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [nums[0]]

        for i in nums[1:]:
            ans.append(ans[-1]+i)
        return ans
