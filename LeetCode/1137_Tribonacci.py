class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        l = [0, 1, 1]

        for i in range(n-2):
            l.append(l[-1]+l[-2]+l[-3])
        return l[-1]
