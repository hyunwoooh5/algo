class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n0, n1, n2 = nums.count(0), nums.count(1), nums.count(2)

        for i in range(n0):
            nums[i] = 0
        for i in range(n1):
            nums[n0+i] = 1
        for i in range(n2):
            nums[n0+n1+i] = 2


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return

        low = 0  # Pointer for the next position for 0 (red)
        mid = 0  # Current element being considered
        high = n - 1  # Pointer for the next position for 2 (blue)

        while mid <= high:
            if nums[mid] == 0:
                # If current element is 0, swap it with the element at 'low'
                # and move both 'low' and 'mid' pointers forward.
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # If current element is 1, it's already in its correct
                # relative position, so just move 'mid' pointer forward.
                mid += 1
            else:  # nums[mid] == 2
                # If current element is 2, swap it with the element at 'high'
                # and move 'high' pointer backward. Do NOT increment 'mid'
                # because the swapped element at 'mid' could be 0, 1, or 2
                # and needs to be re-evaluated.
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
