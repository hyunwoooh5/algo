class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        ans = 0
        for ind, i in enumerate(citations):
            if i >= ind+1:
                ans = ind+1
        return ans
