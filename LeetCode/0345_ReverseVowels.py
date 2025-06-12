class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        s = list(s)
        l, r = 0, len(s)-1

        while l < r:
            while l < r and s[l] not in vowels:
                l += 1
            while r > l and s[r] not in vowels:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)
