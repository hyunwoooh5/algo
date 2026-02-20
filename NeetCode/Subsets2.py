class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        nums.sort()

        n = len(nums)

        def backtrack(start, path):
            for i in range(start, n):
                if nums[i] == nums[i-1] and i > start:
                    continue

                path.append(nums[i])
                res.append(list(path))
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])

        return res
