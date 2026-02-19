class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        for i, h in enumerate(height):
            left, right = max([0]+height[:i]), max(height[i+1:]+[0])

            temp = max(min(left, right) - h, 0)

            res += temp

        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        left, right = 0, len(height)-1

        leftmax, rightmax = height[left], height[right]

        while left < right:
            if leftmax < rightmax:
                left += 1
                leftmax = max(leftmax, height[left])
                res += leftmax-height[left]
            else:
                right -= 1
                rightmax = max(rightmax, height[right])
                res += rightmax - height[right]

        return res
