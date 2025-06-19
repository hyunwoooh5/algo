class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        ans = 0
        n = len(mat)
        for i in range(n):
            ans += mat[i][i] + mat[n-i-1][i]
        if n % 2 == 1:
            ans -= mat[n//2][n//2]

        return ans
