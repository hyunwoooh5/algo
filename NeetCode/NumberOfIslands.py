class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
                return

            grid[i][j] = '0'

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)

        return count


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        from collections import deque

        def bfs(i, j):
            q = deque()
            grid[i][j] = '0'
            q.append((i, j))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    row_new, col_new = row+dr, col+dc

                    if row_new < 0 or col_new < 0 or row_new >= m or col_new >= n or grid[row_new][col_new] == "0":
                        continue

                    q.append((row_new, col_new))
                    grid[row_new][col_new] = "0"

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    count += 1
                    bfs(row, col)

        return count


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0" or grid[i][j] == "#":
                return

            grid[i][j] = "#"

            for dr, dc in directions:
                dfs(i+dr, j+dc)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        from collections import deque

        def bfs(i, j):
            queue = deque([])
            queue.append((i, j))
            grid[i][j] = "0"

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row+dr, col+dc

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        grid[nr][nc] = "0"

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i, j)
                    count += 1

        return count
