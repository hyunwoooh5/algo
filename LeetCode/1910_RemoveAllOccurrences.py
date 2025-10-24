class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ans = []
        if len(part) > 1:
            for char in s:
                print("".join(ans[-(len(part)-1):])+char)
                if "".join(ans[-(len(part)-1):])+char == part:
                    for _ in range(len(part)-1):
                        ans.pop()

                else:
                    ans.append(char)

        elif len(part) == 1:
            for char in s:
                if char != part:
                    ans.append(char)

        return "".join(ans)
