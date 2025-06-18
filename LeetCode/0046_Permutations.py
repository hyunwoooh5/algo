class Solution(object):
    def permute(self, nums):  # Backtracking
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]

        ans = []
        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]
            for p in self.permute(rest):
                ans.append([nums[i]]+p)
        return ans
