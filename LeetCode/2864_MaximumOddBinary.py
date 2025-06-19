class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        c = s.count('1')

        if c == 1:
            return '0'*(n-1)+'1'

        ans = ['0' for _ in range(n-1)] + ['1']
        c -= 1
        ind = 0
        while c > 0:
            ans[ind] = '1'
            ind += 1
            c -= 1
        return "".join(ans)
