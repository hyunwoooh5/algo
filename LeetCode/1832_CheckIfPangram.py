class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = {}
        for char in sentence:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1

        return len(d) == 26
