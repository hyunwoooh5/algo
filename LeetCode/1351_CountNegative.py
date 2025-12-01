class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        def binary_search(row):
            left, right = 0, len(row)-1

            while left <= right:
                mid = (left+right)//2

                if row[mid] >= 0:
                    left = mid+1
                else:
                    right = mid-1

            return len(row) - left

        ans = 0
        for row in grid:
            ans += binary_search(row)

        return ans
