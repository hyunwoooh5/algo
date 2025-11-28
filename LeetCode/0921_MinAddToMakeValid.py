class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        l = []
        for char in s:
            if char == '(':
                l.append('(')
            else:
                if len(l) != 0:
                    l.pop()
                else:
                    ans += 1
        return ans + len(l)
