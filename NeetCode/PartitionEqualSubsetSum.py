class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 == 1:
            return False

        n = len(nums)
        t = s//2
        dp = [False]*(t+1)
        dp[0] = True

        for num in nums:
            for i in range(t, num-1, -1):
                if i-num >= 0 and dp[i-num]:
                    dp[i] = True

        return dp[-1]
