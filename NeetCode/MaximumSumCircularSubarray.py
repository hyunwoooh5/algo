class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr = 0
        m1 = -1e10
        for n in nums:
            curr = max(curr+n, n)
            m1 = max(curr, m1)

        s = sum(nums)

        curr = 0
        m2 = -1e10
        for n in nums:
            curr = max(curr - n, -n)
            m2 = max(curr, m2)

        m2 = s + m2

        if m1 < 0:
            return m1
        else:
            return max(m1, m2)
