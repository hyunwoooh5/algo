class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        ans = 0
        while num > 0:
            num, res = num // 2, num % 2
            ans += 1
            if res == 1:
                ans += 1
        return ans-1
