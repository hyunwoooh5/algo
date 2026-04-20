class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        ans = [intervals[0]]

        for c, d in intervals[1:]:
            prev_a, prev_b = ans[-1]

            if prev_b < c:
                ans.append([c, d])
            else:
                new_a = min(prev_a, c)  # technically prev_a because sorted
                new_b = max(prev_b, d)
                ans[-1] = [new_a, new_b]

        return ans


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        ans = [intervals[0]]

        for left, right in intervals[1:]:
            if left <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], right)
            else:
                ans.append([left, right])

        return ans
