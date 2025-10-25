class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        return nums[-1]*nums[-2] - nums[0]*nums[1]


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        fb, sb = 0, 0
        fs, ss = float(inf), float(inf)

        for n in nums:
            if n < fs:
                fs, ss = n, fs
            elif n < ss:
                ss = n

            if n > fb:
                fb, sb = n, fb
            elif n > sb:
                sb = n

        return fb*sb - fs*ss
