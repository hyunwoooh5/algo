class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p, n = [], []
        ans = []
        for i in nums:
            if i > 0:
                p.append(i)
            else:
                n.append(i)

        for i in range(len(nums)//2):
            ans.append(p[i])
            ans.append(n[i])

        return ans
