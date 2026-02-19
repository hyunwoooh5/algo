class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()

        n = len(nums)

        for i, num in enumerate(nums):
            if i != 0 and nums[i-1] == num:
                continue

            left, right = i+1, n-1

            while left < right:
                s = nums[left]+nums[right]

                if s > -num:
                    right -= 1
                elif s < -num:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result
