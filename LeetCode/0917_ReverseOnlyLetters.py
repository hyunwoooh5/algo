class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

        left, right = 0, len(s)-1
        s = [i for i in s]
        while left < right:
            if s[left] in letters and s[right] in letters:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            else:
                if s[left] not in letters:
                    left += 1
                elif s[right] not in letters:
                    right -= 1
        return ''.join(s)
