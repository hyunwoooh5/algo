class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j] and j-i <= k:
                    return True

        return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = {}

        for i, num in enumerate(nums):
            if num in hash_table:
                if i-hash_table[num] <= k:
                    return True
                else:
                    hash_table[num] = i
            else:
                hash_table[num] = i
        return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        L = 0

        for R in range(len(nums)):
            if R-L > k:
                window.remove(nums[L])
                L += 1

            if nums[R] in window:
                return True

            window.add(nums[R])

        return False
