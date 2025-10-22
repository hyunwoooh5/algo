class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        l = []
        ans = []
        for n in nums:
            if n in l:
                ans.append(n)
                if len(ans) == 2:
                    return ans
            else:
                l.append(n)
