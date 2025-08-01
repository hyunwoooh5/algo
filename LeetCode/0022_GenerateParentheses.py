class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n+1)]
        dp[0] = [""]

        for i in range(1, n+1):
            for j in range(i):
                l1 = dp[j]
                l2 = dp[i-1-j]

                for s1 in l1:
                    for s2 in l2:
                        dp[i].append("("+s1+")"+s2)

        return dp[-1]
