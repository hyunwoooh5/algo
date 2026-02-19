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
