class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)//3
        piles.sort(reverse=True)

        return sum(piles[1:2*n+1:2])
