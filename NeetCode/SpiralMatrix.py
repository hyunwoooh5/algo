class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        top = 0
        bottom = m-1
        left = 0
        right = n-1

        ans = []

        while top <= bottom and left <= right:
            # Right
            for col in range(left, right+1):
                ans.append(matrix[top][col])

            top += 1

            # Down
            for row in range(top, bottom+1):
                ans.append(matrix[row][right])

            right -= 1

            if top <= bottom:

                # Left
                for col in range(right, left-1, -1):
                    ans.append(matrix[bottom][col])

                bottom -= 1

            if left <= right:
                # Up
                for row in range(bottom, top-1, -1):
                    ans.append(matrix[row][left])

                left += 1

        return ans
