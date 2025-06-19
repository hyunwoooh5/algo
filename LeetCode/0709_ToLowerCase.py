class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s.lower()


class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = []
        for i in range(len(s)):
            if ord('A') <= ord(s[i]) <= ord('Z'):
                l.append(chr(ord(s[i])+32))
            else:
                l.append(s[i])

        return "".join(l)
