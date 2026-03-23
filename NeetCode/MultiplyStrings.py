class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        n2 = 0

        for i, n in enumerate(num1[::-1]):
            n1 += int(n)*10**i

        for i, n in enumerate(num2[::-1]):
            n2 += int(n)*10**i

        return str(n1*n2)
