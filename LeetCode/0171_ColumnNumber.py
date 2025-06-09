class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        length = len(columnTitle)
        ans = 0
        for i in range(length):
            num = ord(columnTitle[length-1-i]) - ord('A') + 1
            ans += num*26**i
        return ans
