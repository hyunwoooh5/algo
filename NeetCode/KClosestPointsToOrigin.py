class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        table = [(x**2+y**2, [x, y]) for x, y in points]
        table.sort(key=lambda x: x[0])

        return [table[i][1] for i in range(k)]


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [[x**2+y**2, [x, y]] for x, y in points]

        import heapq
        heapq.heapify(min_heap)

        res = []
        for _ in range(k):
            dist, point = heapq.heappop(min_heap)
            res.append(point)

        return res


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points:
            heapq.heappush(max_heap, [-x**2-y**2, [x, y]])
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        res = []

        while max_heap:
            dist, point = heapq.heappop(max_heap)
            res.append(point)

        return res
