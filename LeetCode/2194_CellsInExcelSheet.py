class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        init = s[:2]
        final = s[-2:]

        ans = []
        for char in range(ord(init[0]), ord(final[0])+1):
            for i in range(int(init[1]), int(final[1])+1):
                ans.append(chr(char)+str(i))

        return ans
