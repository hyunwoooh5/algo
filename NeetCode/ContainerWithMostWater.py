class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        left, right = 0, len(heights)-1

        while left < right:
            temp = min(heights[left], heights[right])*(right-left)
            ans = max(ans, temp)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return ans
