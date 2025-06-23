class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        r, l = 0, 0
        for i in s:
            if i == 'R':
                r += 1
            else:
                l += 1
            if r == l:
                ans += 1
        return ans
