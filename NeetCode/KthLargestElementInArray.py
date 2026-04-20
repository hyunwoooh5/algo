class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        max_heap = [-n for n in nums]

        heapq.heapify(max_heap)

        for _ in range(k-1):
            heapq.heappop(max_heap)

        return -heapq.heappop(max_heap)


class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = [num for num in nums]

        heapq.heapify(min_heap)

        while len(min_heap) > k:
            heapq.heappop(min_heap)

        return min_heap[0]
