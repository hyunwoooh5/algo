class MedianFinder:

    def __init__(self):
        self.small_half = []
        self.large_half = []
        self.count = 0

    def addNum(self, num: int) -> None:

        # push first
        heapq.heappush(self.small_half, -num)

        if self.small_half and self.large_half and -self.small_half[0] > self.large_half[0]:
            val = -heapq.heappop(self.small_half)
            heapq.heappush(self.large_half, val)

        if len(self.small_half) > len(self.large_half) + 1:
            val = -heapq.heappop(self.small_half)
            heapq.heappush(self.large_half, val)

        elif len(self.large_half) > len(self.small_half) + 1:
            val = heapq.heappop(self.large_half)
            heapq.heappush(self.small_half, -val)

        # max(small_half) <= min(large_half)

    def findMedian(self) -> float:
        if len(self.small_half) > len(self.large_half):
            return float(-self.small_half[0])
        elif len(self.large_half) > len(self.small_half):
            return float(self.large_half[0])
        else:
            return (-self.small_half[0] + self.large_half[0]) / 2.0
