class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1, dict2 = {}, {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in dict1:
                if dict1[s[i]] != t[i]:
                    return False
            else:
                dict1[s[i]] = t[i]

        for i in range(len(s)):
            if t[i] in dict2:
                if dict2[t[i]] != s[i]:
                    return False
            else:
                dict2[t[i]] = s[i]

        return True
