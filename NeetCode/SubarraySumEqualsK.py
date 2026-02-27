class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_table = {0: 1}
        curr = 0
        count = 0
        for num in nums:
            curr += num
            if curr - k in hash_table:
                count += hash_table[curr-k]

            if curr in hash_table:
                hash_table[curr] += 1
            else:
                hash_table[curr] = 1

        return count
