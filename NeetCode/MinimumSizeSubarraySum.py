class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        res = n+1
        s = 0

        for right in range(n):
            s += nums[right]

            while s >= target and left <= right:
                res = min(res, right-left+1)

                s -= nums[left]
                left += 1

        if res == n+1:
            return 0
        return res
