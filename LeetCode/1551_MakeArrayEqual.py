class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            return (n//2)**2
        else:
            k = (n-1)//2
            return k*(k+1)
