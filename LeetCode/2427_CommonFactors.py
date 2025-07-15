class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b!=0:
            a, b = b, a%b
        
        ans = 0
        for i in range(1, a+1):
            if a%i==0:
                ans+=1
        return ans