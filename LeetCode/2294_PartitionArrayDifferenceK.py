class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))

        nums.sort()
        count = 0
        init = nums[0]
        for i in nums[1:]:
            if i - init > k:
                count += 1
                init = i

        return count+1
