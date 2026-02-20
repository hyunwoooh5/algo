class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, path):
            if sum(path) == target:
                res.append(list(path))

            for i in range(start, len(candidates)):
                if candidates[i] == candidates[i-1] and i > start:
                    continue

                path.append(candidates[i])

                if sum(path) > target:
                    path.pop()
                    continue

                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])

        return res
