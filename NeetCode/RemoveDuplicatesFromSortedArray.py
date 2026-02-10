class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i += 1

        return len(nums)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 0
        n = len(nums)

        while r < n:
            nums[l] = nums[r]
            while r < n and nums[r] == nums[l]:
                r += 1
            l += 1
        return l
