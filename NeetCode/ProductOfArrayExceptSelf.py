class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n

        for i, num in enumerate(nums[:-1]):
            prefix[i+1] = prefix[i]*num

        for i, num in enumerate(nums[1:][::-1]):
            suffix[n-1-i-1] *= suffix[n-1-i]*num

        result = [prefix[i]*suffix[i] for i in range(n)]

        return result
