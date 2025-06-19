class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        n = len(candyType)
        s = set(candyType)

        if n//2 >= len(s):
            return len(s)
        else:
            return n//2
