class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        n = len(heights)

        for i, h in enumerate(heights):
            w = 1

            if i > 0:
                left = i-1
                while left >= 0 and heights[left] >= h:
                    w += 1
                    left -= 1
            if i < n-1:
                right = i+1
                while right < n and heights[right] >= h:
                    w += 1
                    right += 1

            ans = max(ans, w*h)

        return ans


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        ans = 0

        for i, h in enumerate(heights + [0]):
            start = i

            # When there is a new candidate, calculate previous one
            while stack and stack[-1][1] >= h:
                index, height = stack.pop()

                ans = max(ans, height * (i-index))

                # how far it can go to the left
                start = index

            stack.append((start, h))

        return ans


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        leftmost = [-1]*n

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                leftmost[i] = stack[-1]

            stack.append(i)

        stack = []
        rightmost = [n]*n

        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightmost[i] = stack[-1]

            stack.append(i)

        ans = 0

        for i in range(n):
            ans = max(ans, heights[i] * (rightmost[i]-leftmost[i]-1))

        return ans
