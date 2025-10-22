class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        ans = [[None for _ in range(n-2)] for _ in range(n-2)]

        for i in range(n-2):
            for j in range(n-2):
                ans[i][j] = max([max(g[j:j+3]) for g in grid[i:i+3]])

        return ans
