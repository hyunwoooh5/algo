class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = set()

        for num in nums:
            if num in hash_table:
                return True
            else:
                hash_table.add(num)

        return False


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)

        return False
