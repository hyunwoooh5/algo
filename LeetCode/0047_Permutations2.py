class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]

        ans = []
        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]
            for p in self.permuteUnique(rest):
                if [nums[i]]+p not in ans:
                    ans.append([nums[i]]+p)
        return ans


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()
        used = [False] * n

        def backtrack(path):
            if len(path) == n:
                result.append(list(path))
                return

            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])

        return result
