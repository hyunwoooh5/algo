class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = [i[0] for i in points]

        n.sort()
        a = [n[i+1]-n[i] for i in range(len(n)-1)]
        return max(a)
