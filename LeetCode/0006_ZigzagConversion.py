class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans = ['']*numRows
        index = [i for i in range(numRows)] + \
            [i for i in range(numRows-2, 0, -1)]
        index = index * (len(s)//len(index)+1)

        for i in range(len(s)):
            ans[index[i]] += s[i]
        result = ''
        for i in ans:
            result += i

        return result
