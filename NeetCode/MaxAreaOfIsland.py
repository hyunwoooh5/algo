class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = [0]

        def dfs(i, j, count):

            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return

            grid[i][j] = 0
            count[0] += 1

            dfs(i+1, j, count)
            dfs(i-1, j, count)
            dfs(i, j+1, count)
            dfs(i, j-1, count)

        ans = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    count[0] = 0
                    dfs(row, col, count)

                    ans = max(ans, count[0])

        return ans


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):

            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 0

            grid[i][j] = 0

            area = 1 + dfs(i+1, j)+dfs(i-1, j)+dfs(i, j+1) + dfs(i, j-1)

            return area

        ans = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    ans = max(ans, dfs(row, col))

        return ans


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        from collections import deque

        def bfs(i, j):
            q = deque()
            grid[i][j] = 0
            area = 1
            q.append((i, j))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    row_new, col_new = row + dr, col + dc

                    if row_new < 0 or col_new < 0 or row_new >= m or col_new >= n or grid[row_new][col_new] == 0:
                        continue

                    q.append((row_new, col_new))
                    area += 1
                    grid[row_new][col_new] = 0

            return area

        ans = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    ans = max(ans, bfs(row, col))

        return ans
