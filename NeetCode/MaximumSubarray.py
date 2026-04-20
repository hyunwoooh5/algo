class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        m = -1e9
        for num in nums:
            curr = max(curr+num, num)
            m = max(m, curr)

        return m


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        temp = 0
        for num in nums:
            temp = max(temp+num, num)
            ans = max(ans, temp)

        return ans
