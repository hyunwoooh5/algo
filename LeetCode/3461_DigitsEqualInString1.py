class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = [c for c in s]

        while len(s) > 2:
            for i in range(len(s)-1):
                s[i] = str((int(s[i]) + int(s[i+1])) % 10)
            s.pop()

        return s[0] == s[1]
