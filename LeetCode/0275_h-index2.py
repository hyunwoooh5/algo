class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        ans = 0
        for ind, i in enumerate(citations[::-1]):
            if i >= ind+1:
                ans = ind+1
        return ans
