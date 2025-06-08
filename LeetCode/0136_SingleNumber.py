class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        space = []
        for i in range(len(nums)):
            if nums[i] in space:
                space.remove(nums[i])
            else:
                space.append(nums[i])

        return space[0]


class Solution:
    def singleNumber(self, nums) -> int:
        """
        Finds the single element in a list where every other element appears twice.

        This solution utilizes the bitwise XOR operator. By XORing all elements
        in the list, the duplicate numbers cancel each other out, leaving only the
        unique number.

        XOR: a ^ a = 0, a ^ 0 = a, commutative and associative

        Args:
          nums: A list of integers where each element appears twice except for one.

        Returns:
          The integer that appears only once.
        """
        result = 0
        for num in nums:
            result ^= num
        return result
