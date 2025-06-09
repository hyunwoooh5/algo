import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip().lower()

        s_cleaned = re.sub(r'[^A-Za-z0-9]', '', s)

        return s_cleaned == s_cleaned[::-1]
