class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for interval in intervals:
            last_merged = merged[-1]
            last_end = last_merged[1]

            current_start, current_end = interval

            if current_start <= last_end:
                last_merged[1] = max(current_end, last_end)

            else:
                merged.append(interval)

        return merged
