class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a10, b10 = 0, 0
        for i in range(len(a)):
            a10 += int(a[-i-1])*(2**i)
        for i in range(len(b)):
            b10 += int(b[-i-1])*(2**i)

        sum = a10 + b10
        answer = []
        while sum != 0:
            temp = sum % 2
            sum = sum//2
            answer.append(str(temp))

        print('answer')

        if len(answer) == 0:
            return "0"
        result = ''
        for i in range(len(answer)):
            result = result + answer[-i-1]
        return result


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = int(a, 2) + int(b, 2)
        return bin(ans)[2:]
