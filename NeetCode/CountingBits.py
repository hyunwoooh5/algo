class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)

        for i in range(1, n+1):
            dp[i] = dp[i//2] + i % 2

        return dp


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for num in range(n+1):
            one = 0

            for i in range(32):
                if num & (1 << i):
                    one += 1

            ans.append(one)

        return ans
