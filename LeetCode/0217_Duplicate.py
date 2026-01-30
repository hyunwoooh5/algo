from typing import List


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set(nums)
        if len(nums) == len(s):
            return False
        return True


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = 1

        return False
