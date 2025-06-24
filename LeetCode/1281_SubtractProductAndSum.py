class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(n)
        l = [int(i) for i in n]

        prod, s = 1, 0
        for i in l:
            prod *= i
            s += i
        return prod-s
