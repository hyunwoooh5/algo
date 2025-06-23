class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()

        a = [i[::-1] for i in s]
        ans = a[0]
        for i in a[1:]:
            ans += " "+i
        return ans
