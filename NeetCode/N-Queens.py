class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def backtrack(start, path, cols, pos_diag, neg_diag):
            if start == n:
                res.append(["".join(row) for row in path])
                return

            for c in range(n):
                if c in cols or (start+c) in pos_diag or (start-c) in neg_diag:
                    continue

                cols.add(c)
                pos_diag.add(start+c)
                neg_diag.add(start-c)
                path[start][c] = "Q"

                backtrack(start+1, path, cols, pos_diag, neg_diag)

                cols.remove(c)
                pos_diag.remove(start+c)
                neg_diag.remove(start-c)
                path[start][c] = "."

        backtrack(0, [["."]*n for _ in range(n)], set(), set(), set())

        return res
