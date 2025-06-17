class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = bin(num)
        ans = ['1' if i == '0' else '0' for i in binary]

        return int(''.join(ans[2:]), 2)
