class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev, best = 0, 0

        for num in nums[:-1]:
            temp = max(prev+num, best)
            prev, best = best, temp

        ans = best

        prev, best = 0, 0

        for num in nums[1:]:
            temp = max(prev+num, best)
            prev, best = best, temp

        return max(ans, best)


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)-1

        if n == 0:
            return nums[0]
        elif n == 1:
            return max(nums[0], nums[1])

        dp1 = [0]*n

        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp1[i] = max(dp1[i-2]+nums[i], dp1[i-1])

        dp2 = [0]*n

        dp2[0] = nums[1]
        dp2[1] = max(nums[1], nums[2])

        for i in range(2, n):
            dp2[i] = max(dp2[i-2]+nums[i+1], dp2[i-1])

        return max(dp1[-1], dp2[-1])
