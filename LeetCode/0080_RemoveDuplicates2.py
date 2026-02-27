class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0

        while r < n:
            nums[l] = nums[r]

            count = 1
            r += 1
            while r < n and nums[r] == nums[l]:
                if count == 1:
                    nums[l+1] = nums[r]
                    count += 1
                r += 1
            if count == 1:
                l += 1
            else:
                l += 2
        return l
