class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        e = sum(nums)
        d = sum([int(k) for i in nums for k in str(i)])
        return abs(e-d)
