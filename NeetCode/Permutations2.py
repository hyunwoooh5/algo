class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n = len(nums)
        used = [False]*n

        res = []

        def backtrack(path):
            if len(path) == n:
                res.append(list(path))
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                elif i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                path.append(nums[i])
                used[i] = True
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return res
