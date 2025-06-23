class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        ans = [0, 0]
        d = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] in d:
                    ans[0] = grid[i][j]
                else:
                    d.append(grid[i][j])

        for i in range(1, len(grid)**2+1):
            if i not in d:
                ans[1] = i
                break
        return ans
