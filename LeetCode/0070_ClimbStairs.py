class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        elif n==2:
            return 2
            
        a, b = 1, 2

        # Fibonacci without calling function
        for _ in range(3, n+1):
            a, b = b, a+b
        
        return b