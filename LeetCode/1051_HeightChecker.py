class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        a = [i for i in heights]
        a.sort()

        return sum([a[i] != heights[i] for i in range(len(a))])
