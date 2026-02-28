class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1]+1
        n = len(digits)

        for i in range(n):
            if i != n-1 and digits[n-1-i] == 10:
                digits[n-1-i] = 0
                digits[n-1-i-1] += 1

            if i == n-1 and digits[n-1-i] == 10:
                digits[n-1-i] = 0
                digits.insert(0, 1)

        return digits
