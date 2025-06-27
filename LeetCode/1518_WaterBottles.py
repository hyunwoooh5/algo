class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        empty = 0
        ans = 0
        while numBottles > 0:
            empty += numBottles
            ans += numBottles

            if empty < numExchange:
                break
            else:
                numBottles = empty // numExchange
                empty -= numBottles*numExchange

        return ans
