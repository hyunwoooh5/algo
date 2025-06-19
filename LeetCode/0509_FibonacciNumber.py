class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return self.fib(n-1)+self.fib(n-2)


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1

        for i in range(2, n+1):
            a, b = b, a+b
        return b
