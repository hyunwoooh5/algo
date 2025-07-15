class Solution(object):
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}

        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        vals = d.values()

        for i in vals:
            if i != 1:
                temp = 0
                for j in range(1, i+1):
                    if i % j == 0:
                        temp += 1
                if temp == 2:
                    return True
        return False
