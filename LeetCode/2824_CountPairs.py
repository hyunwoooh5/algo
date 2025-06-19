class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]+nums[j] < target:
                    ans += 1
        return ans
