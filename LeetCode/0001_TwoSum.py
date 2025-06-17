from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create a dictionary to store numbers and their indices
        num_map = {}

        # Iterate through the array with both index and value
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num

            # Check if the complement is already in our dictionary
            if complement in num_map:
                # If found, we have our two numbers.
                # Return the index of the complement and the current index.
                return [num_map[complement], i]

            # If the complement is not found, add the current number and its index to the dictionary
            num_map[num] = i

        # As per the problem constraints, there will always be exactly one solution,
        # so this line should theoretically not be reached.
        return []
