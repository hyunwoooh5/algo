class Solution:
    def sortVowels(self, s: str) -> str:
        vowels, indices = [], []

        for i, char in enumerate(s):
            if char in 'aeiouAEIOU':
                vowels.append(ord(char))
                indices.append(i)

        vowels.sort()
        s = [i for i in s]

        for i, index in enumerate(indices):
            s[index] = chr(vowels[i])

        return "".join(s)
