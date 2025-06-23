class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = bin(n)[2:]
        l = [str(1-int(i)) for i in b]
        return int(''.join(l), 2)
