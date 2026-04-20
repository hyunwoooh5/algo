class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)

            if x != y:
                heapq.heappush(max_heap, x-y)

        if len(max_heap) == 1:
            return -max_heap[0]
        else:
            return 0


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]

        import heapq
        heapq.heapify(stones)

        while len(stones) > 1:
            # x > y
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x == y:
                continue
            else:
                heapq.heappush(stones, -(x-y))

        return -stones[0] if len(stones) == 1 else 0
