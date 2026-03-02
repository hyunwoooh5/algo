class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            result.append(list(path))

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])

        return result


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            result += [subset + [num] for subset in result]

        return result


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(start, path):
            ans.append(list(path))

            for i in range(start, n):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])

        return ans


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(i, path):
            if i>=n:
                ans.append(list(path))
                return

            path.append(nums[i])
            backtrack(i+1, path)
            
            path.pop()
            backtrack(i+1, path)

        backtrack(0, [])        

        return ans