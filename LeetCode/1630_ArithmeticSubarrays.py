class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = [True for i in range(len(l))]

        for i, (left, right) in enumerate(zip(l, r)):
            li = nums[left:right+1]
            li.sort()
            for j in range(len(li)-2):
                if li[j+2]-li[j+1] != li[1] - li[0]:
                    ans[i] = False
                    break
        return ans
