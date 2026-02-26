class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [n+1] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                if j+nums[j] >= i:
                    dp[i] = min(dp[i], dp[j]+1)

        return dp[-1]


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])

            l = r+1
            r = farthest
            res += 1
        return res
