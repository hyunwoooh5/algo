class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum = [0]

        for i in nums[:-1]:
            leftsum.append(leftsum[-1]+i)

        rightsum = [0]

        for j in nums[1:][::-1]:
            rightsum.append(rightsum[-1]+j)

        rightsum = rightsum[::-1]

        return [abs(leftsum[i]-rightsum[i]) for i in range(len(nums))]
