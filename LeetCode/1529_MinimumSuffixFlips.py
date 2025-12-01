class Solution:
    def minFlips(self, target: str) -> int:
        ans = 0

        for i in range(len(target)):
            if target[i] == '1':
                if ans % 2 == 0:
                    ans += 1
            else:
                if ans % 2 == 1:
                    ans += 1

        return ans
