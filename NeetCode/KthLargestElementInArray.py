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
