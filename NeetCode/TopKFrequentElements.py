class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}

        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1

        import heapq

        max_heap = []

        for key, value in hash_table.items():
            heapq.heappush(max_heap, (-value, key))

        result = []

        for _ in range(k):
            _, num = heapq.heappop(max_heap)
            result.append(num)

        return result


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}

        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1

        import heapq

        max_heap = []

        for key, value in hash_table.items():
            heapq.heappush(max_heap, (-value, key))

        ans = []

        for _ in range(k):
            freq, e = heapq.heappop(max_heap)
            ans.append(e)

        return ans


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}

        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1

        import heapq

        min_heap = []

        for key, value in hash_table.items():
            heapq.heappush(min_heap, (value, key))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        ans = []

        for i in range(k):
            ans.append(min_heap[i][1])

        return ans
