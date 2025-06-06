class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0

        maxlen = 1

        for i in range(len(s)):
            count = 0
            l = []
            for j in range(i+1, len(s)):
                count += 1
                l.append(s[j-1])
                if j == len(s)-1:
                    if not (s[j] in l):
                        count += 1
                    if count > maxlen:
                        maxlen = count
                elif s[j] in l:
                    if count > maxlen:
                        maxlen = count
                    break

        return maxlen
