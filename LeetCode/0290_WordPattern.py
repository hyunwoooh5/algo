class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()
        d = {}
        if len(pattern) != len(s):
            return False

        for i in range(len(s)):
            if pattern[i] in d:
                if d[pattern[i]] != s[i]:
                    return False
            else:
                d[pattern[i]] = s[i]

        d_inv = {}
        for i in range(len(s)):
            if s[i] in d_inv:
                if d_inv[s[i]] != pattern[i]:
                    return False
            else:
                d_inv[s[i]] = pattern[i]

        return True
