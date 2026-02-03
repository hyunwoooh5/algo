class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 0

        for num in nums:
            if num-1 in nums:
                continue
            else:
                i = 1
                temp = 1
                while True:
                    if num+i in nums:
                        temp += 1
                        i += 1
                    else:
                        result = max(result, temp)
                        break

        return result
