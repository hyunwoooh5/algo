class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        ans = [0]*len(s)
        for ind, i in enumerate(indices):
            ans[i] = s[ind]

        return "".join(ans)
