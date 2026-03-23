class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)+1

        s = set(nums)

        for i in range(n):
            if i not in s:
                return i


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        return n*(n+1)//2 - sum(nums)
