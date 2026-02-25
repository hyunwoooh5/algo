class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = n

        for i in range(n):
            l, r = i-1, i+1

            while l >= 0 and r < n:
                if s[l] == s[r]:
                    ans += 1
                    l -= 1
                    r += 1
                else:
                    break

            l, r = i-1, i

            while l >= 0 and r < n:
                if s[l] == s[r]:
                    ans += 1
                    l -= 1
                    r += 1
                else:
                    break

        return ans


class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        n = len(s)

        dp = [[False]*n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    ans += 1

        return ans
