class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        even = sum([int(i) for i in num[::2]])
        odd = sum([int(i) for i in num[1::2]])

        return even == odd
