class Solution:
    def kthCharacter(self, k: int) -> str:
        from math import log2, ceil
        word = 'a'
        for i in range(ceil(log2(k))):
            word = word + \
                "".join([chr((ord(char)-ord('a')+1) % 26 + ord('a'))
                        for char in word])

        return word[k-1]
