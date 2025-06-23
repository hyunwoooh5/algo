class Solution(object):
    def minDeletion(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d = {}
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1

        counts = list(d.values())
        counts.sort()
        ans, ind = 0, 0
        while len(counts)-ind > k:
            ans += counts[ind]
            ind += 1

        return ans
