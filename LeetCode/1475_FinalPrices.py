class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)

        ans = []

        for i in range(n):
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    ans.append(prices[i]-prices[j])
                    break
            if len(ans) != (i+1):
                ans.append(prices[i])

        return ans
