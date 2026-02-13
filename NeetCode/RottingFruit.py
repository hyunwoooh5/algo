class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        from collections import deque

        queue = deque([])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        num1 = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j])
                elif grid[i][j] == 1:
                    num1 += 1

        if num1 == 0:
            return 0

        count = 0
        while queue and num1 > 0:
            count += 1

            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append([nr, nc])
                        num1 -= 1

        return count if num1 == 0 else -1
