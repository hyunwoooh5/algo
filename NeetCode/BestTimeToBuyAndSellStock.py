class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        ans = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                ans = max(ans, prices[r]-prices[l])
            else:
                l = r
            r += 1

        return ans


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minbuy = prices[0]

        for p in prices:
            ans = max(ans, p - minbuy)
            minbuy = min(p, minbuy)

        return ans


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minbuy = prices[0]

        for price in prices:
            ans = max(ans, price-minbuy)
            minbuy = min(minbuy, price)

        return ans


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        l, r = 0, 1
        ans = 0
        while r < n:
            if prices[r] > prices[l]:
                ans = max(ans, prices[r]-prices[l])
            else:
                l = r  # found a cheaper place
            r += 1
        return ans
