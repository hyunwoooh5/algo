class Solution(object):
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        count = 0

        while ans < n:
            count+=1
            ans +=count

        return count