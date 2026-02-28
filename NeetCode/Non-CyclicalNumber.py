class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def helper(n):
            return sum([int(char)**2 for char in str(n)])

        while n != 1:
            n = helper(n)

            if n not in seen:
                seen.add(n)
            else:
                return False

        return True
