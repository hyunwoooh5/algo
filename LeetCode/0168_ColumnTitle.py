class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        ans = ''
        while columnNumber >= 1:
            p, q = columnNumber//26, columnNumber % 26
            if q == 0:
                q = 26
                p = p-1
            ans += chr(64+q)
            columnNumber = p

        return ans[::-1]
