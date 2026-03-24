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


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        a = [1]*n
        b = [1]*n

        for i, num in enumerate(nums[:-1]):
            a[i+1] = a[i] * num

        for i, num in enumerate(nums[1:][::-1]):
            b[n-1-i-1] = b[n-1-i]*num

        ans = [a[i]*b[i] for i in range(n)]

        return ans
