class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n = n//2
        return count


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        for i in range(32):
            mask = 1 << i

            if mask & n:
                count += 1

        return count


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            count += 1 if n & 1 else 0

            n >>= 1  # shift by 1

        return count


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            n = n & (n-1)  # remove the rightmost 1 bit

            count += 1

        return count
