class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        zeros = '0'*(32-len(binary))
        return int((zeros+binary)[::-1], 2)
