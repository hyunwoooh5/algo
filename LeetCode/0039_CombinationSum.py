class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            if sum(path) == target:
                result.append(list(path))
                return
            elif sum(path) > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path)
                path.pop()

        backtrack(0, [])

        return result
