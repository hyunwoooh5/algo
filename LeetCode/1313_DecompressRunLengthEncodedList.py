class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        freqval = [[nums[2*i], nums[2*i+1]] for i in range(len(nums)//2)]
        ans = []
        for f, v in freqval:
            for _ in range(f):
                ans.append(v)

        return ans
