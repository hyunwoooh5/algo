class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31-1

        m, n = len(grid), len(grid[0])

        from collections import deque

        queue = deque([[i, j] for i in range(m)
                      for j in range(n) if grid[i][j] == 0])

        while queue:
            r, c = queue.popleft()

            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nr, nc = r + dr, c+dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c]+1
                    queue.append([nr, nc])
