class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = -1

        for i, s in enumerate(word):
            if s == ch:
                index = i
                break

        return word[:index+1][::-1]+word[index+1:]
