class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[1]]

        for i in range(1, numRows):
            temp = [1]
            for j in range(1, i):
                temp.append(ans[i-1][j] + ans[i-1][j-1])
            temp.append(1)

            ans.append(temp)

        return ans
