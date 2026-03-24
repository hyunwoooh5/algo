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


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        s = s.lower()

        while left <= right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1

            else:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False

        return True
