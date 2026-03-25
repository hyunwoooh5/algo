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


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0

        hash_table = {}  # last index of each character

        for r in range(len(s)):
            if s[r] in hash_table and hash_table[s[r]] >= l:
                l = hash_table[s[r]]+1  # move forward

            hash_table[s[r]] = r

            ans = max(ans, r-l+1)

        return ans


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0

        charset = set()

        for r in range(len(s)):
            while s[r] in charset:  # charset is ordered
                charset.remove(s[l])
                l += 1

            charset.add(s[r])
            ans = max(ans, r-l+1)

        return ans
