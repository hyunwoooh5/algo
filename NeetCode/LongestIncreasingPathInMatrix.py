class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        memo = {}

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return

            if (r, c) in memo:
                return memo[(r, c)]

            max_len = 1

            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nr, nc = r + dr, c+dc

                if 0 <= nr < m and 0 <= nc < n and matrix[r][c] < matrix[nr][nc]:
                    max_len = max(max_len, 1 + dfs(nr, nc))

            memo[(r, c)] = max_len

            return max_len

        for row in range(m):
            for col in range(n):
                dfs(row, col)

        return max(memo.values())
