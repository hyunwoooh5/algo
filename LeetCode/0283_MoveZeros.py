class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ans = []

        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                ans.append(nums[i])
            else:
                count += 1
        print(ans)

        for i in range(len(ans)):
            nums[i] = ans[i]
        for j in range(len(ans), len(nums)):
            nums[j] = 0
