class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        queue = [(grid[0][0], 0, 0)]

        import heapq

        visited = [[False]*n for _ in range(m)]
        visited[0][0] = True

        while queue:
            h, r, c = heapq.heappop(queue)

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r_new, c_new = r+dr, c+dc
                if r_new >= 0 and r_new < m and c_new >= 0 and c_new < n and not visited[r_new][c_new]:
                    if r_new == m-1 and c_new == n-1:
                        return max(h, grid[r_new][c_new])
                    heapq.heappush(
                        queue, (max(h, grid[r_new][c_new]), r_new, c_new))
                    visited[r_new][c_new] = True


# Binary search + BFS
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        low, high = 0, m*n-1

        def check(h):
            if grid[0][0] > h:
                return False

            queue = deque([(0, 0)])
            visited = [[False]*n for _ in range(m)]
            visited[0][0] = True

            while queue:
                r, c = queue.popleft()
                if r == m-1 and c == n-1:
                    return True

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] <= h:
                        queue.append((nr, nc))
                        visited[nr][nc] = True

            return False

        ans = high
        while low <= high:
            mid = (low+high)//2

            if check(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1

        return ans


# Binary search + DFS
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        low, high = 0, m*n-1

        visited = [[False]*n for _ in range(m)]

        def check(point, h):
            r, c = point

            if r < 0 or r >= m or c < 0 or c >= n or visited[r][c] or grid[r][c] > h:
                return False
            if r == m-1 and c == n-1:
                return True

            visited[r][c] = True

            return check((r+1, c), h) or check((r-1, c), h) or check((r, c+1), h) or check((r, c-1), h)

        ans = high
        while low <= high:
            mid = (low+high)//2

            if check((0, 0), mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1

            visited = [[False]*n for _ in range(m)]

        return ans
