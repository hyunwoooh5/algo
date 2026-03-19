class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_w1, len_w2 = len(word1), len(word2)

        dp = [[0]*(len_w2+1) for _ in range(len_w1+1)]

        # initialize: if word2==""
        for i in range(1, len_w1+1):
            dp[i][0] = i

        # initialize: if word1==""
        for j in range(1, len_w2+1):
            dp[0][j] = j

        for i in range(1, len_w1+1):
            for j in range(1, len_w2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    insert = dp[i][j-1]
                    delete = dp[i-1][j]
                    replace = dp[i-1][j-1]
                    dp[i][j] = 1 + min(insert, delete, replace)

        return dp[-1][-1]
