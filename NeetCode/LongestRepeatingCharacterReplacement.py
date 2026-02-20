class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        count = {}
        max_freq = 0
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1

            max_freq = max(max_freq, count[s[r]])

            if (r-l+1) - max_freq > k:  # window length - max_freq
                count[s[l]] -= 1
                l += 1

        return r-l+1
