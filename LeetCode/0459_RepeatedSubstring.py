class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s)):
            repeat = len(s)//i
            if s == s[:i]*repeat:
                return True
        return False
