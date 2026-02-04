class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        left, right = 0, m*n-1

        while left <= right:
            mid = (left+right)//2

            a, b = mid//n, mid % n

            if matrix[a][b] == target:
                return True
            elif matrix[a][b] > target:
                right = mid-1
            else:
                left = mid+1

        return False
