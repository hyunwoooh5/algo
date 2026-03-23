class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # transpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # change columns
        for row in range(n):
            for j in range(n//2):
                matrix[row][j], matrix[row][n-1 -
                                            j] = matrix[row][n-1-j], matrix[row][j]
