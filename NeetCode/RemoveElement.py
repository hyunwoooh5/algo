class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, 0
        n = len(nums)

        while r < n:
            while r < n and nums[r] == val:
                r += 1
            if r < n:
                nums[l] = nums[r]
                l += 1
                r += 1
        return l


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0

        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            if nums[l] == val:
                r -= 1
                nums[l] = nums[r]
            else:
                l += 1
        return l


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1

            else:
                l += 1

        return l
