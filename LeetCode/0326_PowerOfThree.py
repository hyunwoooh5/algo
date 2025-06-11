class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        while n != 1:
            n, r = n//3, n % 3

            if r != 0:
                return False
        return True
