class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[1]-x[0])

        ans = []

        for query in queries:
            done = False
            for i in range(len(intervals)):
                if intervals[i][0] <= query <= intervals[i][1]:
                    ans.append(intervals[i][1]-intervals[i][0]+1)
                    done = True
                    break
            if not done:
                ans.append(-1)

        return ans


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()

        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])

        ans = [-1] * len(queries)

        min_heap = []
        i = 0

        for q, original_idx in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                heapq.heappush(min_heap, (end-start+1, end))
                i += 1

            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            if min_heap:
                ans[original_idx] = min_heap[0][0]

        return ans
