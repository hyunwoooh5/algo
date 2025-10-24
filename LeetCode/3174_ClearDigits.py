class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []
        for c in s:
            if c in '1234567890':
                if len(ans) == 0:
                    ans.append(c)
                else:
                    ans.pop()
            else:
                ans.append(c)

        return ''.join(ans)
