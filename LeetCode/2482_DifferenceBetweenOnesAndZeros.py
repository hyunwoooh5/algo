class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid[0])
        n = len(grid)

        col = [0] * m
        row = [0] * n

        for i in range(n):
            for j in range(m):
                row[i] += 1 if grid[i][j] == 1 else -1
                col[j] += 1 if grid[i][j] == 1 else -1

        ans = [[col[j]+row[i] for j in range(m)] for i in range(n)]

        return ans
