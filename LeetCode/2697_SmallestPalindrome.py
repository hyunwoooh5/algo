class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        length = len(s)

        ans = [c for c in s]

        for i in range(length//2):
            x, y = ans[i], ans[length-i-1]
            if x != y:
                if x < y:
                    ans[length-i-1] = x
                else:
                    ans[i] = y
        return ''.join(ans)
