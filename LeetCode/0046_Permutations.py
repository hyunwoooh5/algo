class Solution(object):
    def permute(self, nums):  # Backtracking
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]

        ans = []
        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]
            for p in self.permute(rest):
                ans.append([nums[i]]+p)
        return ans


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        used = [False] * n

        def backtrack(path):
            if len(path) == n:
                result.append(list(path))
                return

            for i in range(n):
                if used[i] == False:
                    path.append(nums[i])
                    used[i] = True
                    backtrack(path)
                    path.pop()
                    used[i] = False

        backtrack([])

        return result
