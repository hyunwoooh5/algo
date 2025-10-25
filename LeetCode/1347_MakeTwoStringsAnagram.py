class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d_s, d_t = {}, {}

        for c in s:
            if c in d_s:
                d_s[c] += 1
            else:
                d_s[c] = 1

        for c in t:
            if c in d_t:
                d_t[c] += 1
            else:
                d_t[c] = 1

        ans = len(t)

        for c in d_s:
            if c in d_t:
                ans -= min(d_s[c], d_t[c])

        return ans
