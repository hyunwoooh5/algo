class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        zeros = '0'*(32-len(binary))
        return int((zeros+binary)[::-1], 2)


class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""

        for i in range(32):
            mask = 1 << i  # push 1 i times to the left (mask)

            if n & mask:  # check ith bit if it is 1
                binary += "1"
            else:
                binary += "0"

        ans = 0

        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                ans |= (1 << i)  # update ith bit

        return ans
