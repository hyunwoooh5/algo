class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = sum([int(i) for i in str(x)])
        if x%s==0:
            return s
        else:
            return -1
        