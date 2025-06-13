class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        sum, i = 0, 1
        while sum < n:
            sum += i
            i += 1

        return i-1 if sum == n else i-2
