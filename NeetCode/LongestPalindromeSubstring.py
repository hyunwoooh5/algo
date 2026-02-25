class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = 1
        best = s[0]

        n = len(s)

        for i in range(n):
            temp = 1
            l, r = i-1, i+1

            while l >= 0 and r <= n-1:
                if s[l] != s[r]:
                    break

                temp += 2

                if temp > ans:
                    ans = temp
                    best = s[l:r+1]

                l -= 1
                r += 1

            l, r = i-1, i
            temp = 0

            while l >= 0 and r <= n-1:
                if s[l] != s[r]:
                    break

                temp += 2

                if temp > ans:
                    ans = temp
                    best = s[l:r+1]

                l -= 1
                r += 1

        return best


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans_left, ans_right = 0, 0

        n = len(s)

        dp = [[False]*n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True

                    if (ans_right - ans_left) < (j-i+1):
                        ans_left = i
                        ans_right = j

        return s[ans_left: ans_right+1]
