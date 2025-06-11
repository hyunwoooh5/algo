class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = [i for i in s]
        t = [j for j in t]
        s.sort()
        t.sort()
        return s == t
