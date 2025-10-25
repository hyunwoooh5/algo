class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        s = text.split()
        ans = 0
        for word in s:
            count = 0
            for char in brokenLetters:
                if char in word:
                    count += 1
                    break
            if count == 0:
                ans += 1
        return ans
