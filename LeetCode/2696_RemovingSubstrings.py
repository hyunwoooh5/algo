class Solution:
    def minLength(self, s: str) -> int:
        ans = []
        for char in s:
            if "".join(ans[-1:])+char == "AB" or "".join(ans[-1:]) + char == "CD":
                ans.pop()
            else:
                ans.append(char)

        return len(ans)
