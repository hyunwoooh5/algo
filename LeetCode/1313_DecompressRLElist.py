class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)//2):
            freq, val = nums[2*i], nums[2*i+1]
            for _ in range(freq):
                ans.append(val)
        return ans
