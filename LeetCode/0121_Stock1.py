class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        ans = 0

        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > ans:
                ans = i - min_price
        return ans

        ans = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                price = prices[j] - prices[i]
                if price > ans:
                    ans = price
        return ans


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = prices[0]
        for price in prices[1:]:
            if price > min_price:
                if price - min_price > ans:
                    ans = price - min_price
            else:
                if min_price > price:
                    min_price = price
        
        return ans