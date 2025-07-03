class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        ans = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = matrix[j][i]
        return ans
