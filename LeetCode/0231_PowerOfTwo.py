class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False

        while n != 1:
            n, r = n//2, n % 2
            if r != 0:
                return False

        return True
