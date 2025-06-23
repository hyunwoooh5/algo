class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [int(i) for i in str(n)]
        l.sort()
        return l[-1]*l[-2]
