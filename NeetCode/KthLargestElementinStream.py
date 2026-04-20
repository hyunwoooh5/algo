class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        import heapq
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = nums
        self.k = k

        heapq.heapify(self.stream)

        while len(self.stream) > self.k:
            heapq.heappop(self.stream)

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)

        if len(self.stream) > self.k:
            heapq.heappop(self.stream)

        return self.stream[0]
