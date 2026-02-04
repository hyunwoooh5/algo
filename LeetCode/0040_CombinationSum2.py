class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(start, path):
            if sum(path) == target:
                result.append(list(path))
                return
            elif sum(path) > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])

        return result


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []

        def backtrack(start, path):
            if sum(path) == target:
                result.append(list(path))

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

        return result
