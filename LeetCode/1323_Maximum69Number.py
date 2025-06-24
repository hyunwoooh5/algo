class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = [i for i in str(num)]

        for i in range(len(n)):
            if n[i] == '6':
                n[i] = '9'
                break

        return int(''.join(n))
