class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}

        for i, num in enumerate(nums):
            if num in hash_table:
                return [hash_table[num], i]
            else:
                hash_table[target-num] = i
        
        return []