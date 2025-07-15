class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        l = []

        for i in s:
            if i == '(':
                l.append(i)
                ans = max(ans, len(l))
            elif i == ')':
                l.pop()
        return ans
