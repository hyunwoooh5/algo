class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        s = s.lower()

        alphanumeric = set(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

        while left <= right:
            if s[left] not in alphanumeric:
                left += 1
            elif s[right] not in alphanumeric:
                right -= 1
            else:
                if s[left] != s[right]:
                    return False
                else:
                    left += 1
                    right -= 1

        return True
