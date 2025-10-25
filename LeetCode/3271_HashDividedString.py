class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        ss = []

        for i in range(n//k):
            ss.append(s[i*k:(i+1)*k])

        hashedChar = [sum([ord(c) - ord('a') for c in i]) %
                      26 + ord('a') for i in ss]

        ss = [chr(ch) for ch in hashedChar]

        return "".join(ss)
