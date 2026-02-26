class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        m = -1e9
        for num in nums:
            curr = max(curr+num, num)
            m = max(m, curr)

        return m
