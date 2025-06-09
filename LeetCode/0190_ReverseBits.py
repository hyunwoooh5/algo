class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary = bin(n)[2:]
        zeros = '0'*(32-len(binary))
        ans = zeros+binary
        return int(ans[::-1], 2)


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(n[::-1], 2)
