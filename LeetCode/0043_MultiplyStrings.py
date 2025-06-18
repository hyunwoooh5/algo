class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = [int(n)*10**index for index, n in enumerate(num1[::-1])]
        n2 = [int(n)*10**index for index, n in enumerate(num2[::-1])]

        return str(sum(n1)*sum(n2))
