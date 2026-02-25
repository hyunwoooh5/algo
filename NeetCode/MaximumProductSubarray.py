class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -1e9
        n = len(nums)

        import math

        for i in range(n):
            for j in range(i+1, n+1):
                res = max(res, math.prod(nums[i:j]))

        return res


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max, curr_min = 1, 1

        res = nums[0]

        for num in nums:
            curr_max, curr_min = max(
                curr_max * num, num*curr_min, num), min(curr_max * num, num*curr_min, num)

            res = max(curr_max, res)

        return res
