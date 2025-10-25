class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ""
        for i in s:
            if i.isdigit():
                ans += chr(int(i)+ord(ans[-1]))
            else:
                ans += i

        return ans
