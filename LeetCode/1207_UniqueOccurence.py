class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        ans = list(d.values())
        return len(ans) == len(set(ans))
