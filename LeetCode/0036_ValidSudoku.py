class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = [str(i) for i in range(1, 10)]

        dict_row = {i: set() for i in range(9)}
        dict_col = {i: set() for i in range(9)}
        dict_box = {i: set() for i in range(9)}

        for r in range(9):
            for c in range(9):
                if board[r][c] in nums:
                    if int(board[r][c]) in dict_row[r]:
                        return False
                    else:
                        dict_row[r].add(int(board[r][c]))

                    if int(board[r][c]) in dict_col[c]:
                        return False
                    else:
                        dict_col[c].add(int(board[r][c]))

                    box_index = (r // 3) * 3 + (c // 3)

                    if int(board[r][c]) in dict_box[box_index]:
                        return False
                    else:
                        dict_box[box_index].add(int(board[r][c]))

        return True
