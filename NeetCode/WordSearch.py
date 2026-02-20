class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        n_word = len(word)

        def backtrack(r, c, k):
            if k == n_word:
                return True

            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != word[k]:
                return False

            # backtracking
            temp = board[r][c]
            board[r][c] = "#"

            res = backtrack(r+1, c, k+1) or backtrack(r-1, c, k +
                                                      1) or backtrack(r, c+1, k+1) or backtrack(r, c-1, k+1)

            board[r][c] = temp

            return res

        for r in range(m):
            for c in range(n):
                if backtrack(r, c, 0):
                    return True

        return False
