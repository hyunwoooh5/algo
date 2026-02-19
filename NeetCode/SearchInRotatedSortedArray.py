class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right-left)//2

            if nums[right] < nums[mid]:
                if nums[left] <= target and nums[mid] >= target:
                    right = mid-1
                else:
                    left = mid + 1

            else:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1

            if nums[mid] == target:
                return mid

        return -1
