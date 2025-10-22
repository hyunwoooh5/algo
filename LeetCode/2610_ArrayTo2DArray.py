class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        m = max(d.values())

        ans = [[] for i in range(m)]

        for i in d.keys():
            for j in range(d[i]):
                ans[j].append(i)

        return ans
