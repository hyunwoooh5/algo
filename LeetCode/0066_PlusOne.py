class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num += int(digits[-i-1])*(10**i)

        num += 1

        return [int(i) for i in str(num)]
