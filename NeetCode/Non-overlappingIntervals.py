class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:  x[1])
        prev_start, prev_end = intervals[0]

        ans = 0

        for start, end in intervals[1:]:
            if prev_end <= start:
                prev_start, prev_end = start, end
            else:
                ans += 1

        return ans


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        curr = [intervals[0][0], intervals[0][1]]
        ans = 0

        for left, right in intervals[1:]:
            if left < curr[1]:
                ans += 1
            else:
                curr = [left, right]

        return ans
