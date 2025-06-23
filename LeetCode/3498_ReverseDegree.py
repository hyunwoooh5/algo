class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for ind, w in enumerate(s):
            ans += (26 - (ord(w)-ord('a')))*(ind+1)
        return ans
