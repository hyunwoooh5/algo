class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = 0
        left = 0
        right = sum(nums[1:])

        if left == right:
            return pivot

        for pivot in range(1, len(nums)):
            left += nums[pivot-1]
            right -= nums[pivot]

            if left == right:
                return pivot
        return -1
