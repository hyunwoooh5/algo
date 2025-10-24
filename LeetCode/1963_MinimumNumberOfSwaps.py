class Solution:
    def minSwaps(self, s: str) -> int:
        ans = 0

        for char in s:
            if char == '[':
                ans += 1
            elif ans > 0:
                ans -= 1

        return (ans + 1)//2
