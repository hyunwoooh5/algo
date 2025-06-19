class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        n = r*c
        flatten = [0]*n
        mat_row, mat_col = len(mat), len(mat[0])

        if n != mat_row*mat_col:
            return mat

        for i in range(mat_row):
            for j in range(mat_col):
                flatten[i*mat_col+j] = mat[i][j]

        ans = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                ans[i][j] = flatten[i*c+j]

        return ans
