class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = [str(i) for i in range(1, 10)]

        dict_row = {i: set() for i in range(9)}
        dict_col = {i: set() for i in range(9)}
        dict_box = {i: set() for i in range(9)}

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num in nums:
                    if num in dict_row[r]:
                        return False
                    else:
                        dict_row[r].add(num)

                    if num in dict_col[c]:
                        return False
                    else:
                        dict_col[c].add(num)

                    index = 3*(r//3) + (c//3)

                    if num in dict_box[index]:
                        return False
                    else:
                        dict_box[index].add(num)

        return True
