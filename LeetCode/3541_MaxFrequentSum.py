class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = 'aeiou'
        v = {}
        c = {}
        for w in s:
            if w in vowels:
                if w in v:
                    v[w] += 1
                else:
                    v[w] = 1
            else:
                if w in c:
                    c[w] += 1
                else:
                    c[w] = 1

        return max(list(v.values())+[0]) + max(list(c.values())+[0])
