class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        divisors = []
        if num == 1:
            return False

        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                divisors.append(i)
                divisors.append(num//i)

        return sum(divisors) == 2*num
