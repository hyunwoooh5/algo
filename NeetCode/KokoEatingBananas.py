class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = left + (right-left)//2
            t = sum((b+mid-1)//mid for b in piles)
            if t <= h:
                right = mid
            else:
                left = mid+1
        return right
