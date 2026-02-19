class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        hash_table = {}

        for r in range(len(s)):
            if s[r] in hash_table and hash_table[s[r]] >= l:
                l = hash_table[s[r]]+1

            hash_table[s[r]] = r

            ans = max(ans, r-l+1)

        return ans
