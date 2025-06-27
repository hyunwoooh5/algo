class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        current = 1
        ans = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                current += 1
                ans = max(ans, current)
            else:
                current = 1

        return ans
