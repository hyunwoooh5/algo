class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count = [[s.count("0"), s.count("1")] for s in strs]

        dp = [[0]*(n+1) for _ in range(m+1)]

        for zeros, ones in count:
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i >= zeros and j >= ones:
                        dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)

        return dp[-1][-1]
