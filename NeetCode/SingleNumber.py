class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = {}

        for num in nums:
            if num in s:
                s[num] += 1
            else:
                s[num] = 1

        for num in s:
            if s[num] == 1:
                return num


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            ans = num ^ ans

        return ans
