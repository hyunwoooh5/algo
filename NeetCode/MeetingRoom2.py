"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        ans = [[[intervals[0].start, intervals[0].end]]]

        for interval in intervals[1:]:
            start, end = interval.start, interval.end
            done = False
            for j in ans:
                prev_start, prev_end = j[-1]
                if prev_end <= start:
                    j.append([start, end])
                    done = True
                    break

            if not done:
                ans.append([[start, end]])

        return len(ans)


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        import heapq

        rooms = []

        heapq.heappush(rooms, intervals[0].end)

        for i in range(1, len(intervals)):
            if intervals[i].start >= rooms[0]:
                heapq.heappop(rooms)

            heapq.heappush(rooms, intervals[i].end)

        return len(rooms)


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        rooms = [intervals[0]]

        for interval in intervals[1:]:
            done = False
            for i in range(len(rooms)):
                room = rooms[i]
                if room.end <= interval.start:
                    rooms[i] = interval
                    done = True
                    break

            if not done:
                rooms.append(interval)

        return len(rooms)
