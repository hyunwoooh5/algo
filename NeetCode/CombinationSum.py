class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            # Base
            if sum(path) == target:
                result.append(list(path))

            # recursive
            for i in range(start, len(nums)):
                path.append(nums[i])

                # pruning
                if sum(path) > target:
                    path.pop()
                    continue

                backtrack(i, path)
                path.pop()

        backtrack(0, [])

        return result
