class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        left, right = 0, len(s)
        ans = []

        for char in s:
            if char == 'I':
                ans.append(left)
                left += 1
            else:
                ans.append(right)
                right -= 1

        ans.append(left)

        return ans
