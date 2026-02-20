class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(nums, path):
            if len(path) == n:
                res.append(list(path))
                return

            for i in range(len(nums)):
                path.append(nums[i])

                backtrack(nums[:i]+nums[i+1:], path)
                path.pop()

        backtrack(nums, [])
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        used = [False]*n

        def backtrack(path):
            if len(path) == n:
                res.append(list(path))
                return

            for i in range(n):
                if used[i] == False:
                    path.append(nums[i])
                    used[i] = True

                    backtrack(path)
                    path.pop()
                    used[i] = False

        backtrack([])
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(start):
            if start == n:
                res.append(list(nums))
                return

            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]

                backtrack(start + 1)

                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        nums.sort()

        n=len(nums)

        def backtrack(start, path):
            for i in range(start, n):
                if nums[i]==nums[i-1] and i>start:
                    continue
                
                path.append(nums[i])
                res.append(list(path))
                backtrack(i+1, path)
                path.pop()
            

        backtrack(0, [])

        return res