class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return s[:k][::-1]+s[k:]

# Two pointer
class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        left, right = 0, k-1

        s = [char for char in s]
        
        while left <= right:
            s[left], s[right] = s[right], s[left]

            left +=1
            right -=1

        return "".join(s)