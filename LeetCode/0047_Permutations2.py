class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]

        ans = []
        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]
            for p in self.permuteUnique(rest):
                if [nums[i]]+p not in ans:
                    ans.append([nums[i]]+p)
        return ans
