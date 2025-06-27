class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0]*len(nums)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i != j:
                    if nums[i] > nums[j]:
                        ans[i] += 1
                    elif nums[i] < nums[j]:
                        ans[j] += 1

        return ans
