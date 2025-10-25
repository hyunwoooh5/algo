class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        d = {}
        for char in s:
            d[int(char[-1])] = char[:-1]

        sorted_keys = sorted(d)

        return " ".join([d[i] for i in sorted_keys])
