class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        bn = bin(n)[2:]

        if n==1:
            return 0

        for ind, i in enumerate(bn):
            temp = 0
            if i=='1':
                for ind2 in range(ind+1, len(bn)):
                    temp +=1
                    if bn[ind2]=='1':
                        break
                if ind2 == len(bn)-1 and bn[-1]=='0':
                    temp = 0
           
            ans = max(ans, temp)

        return ans