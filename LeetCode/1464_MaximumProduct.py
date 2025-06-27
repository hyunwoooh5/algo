class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [i-1 for i in nums]
        ans = -2**31
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                ans = max(ans, nums[i]*nums[j])

        return ans


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [i-1 for i in nums]
        m1, m2 = 0, 0
        for i in nums:
            if i >= m1:
                m1, m2 = i, m1
            if i < m1 and i >= m2:
                m2 = i
        return m1*m2
