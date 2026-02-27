class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency_list = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            adjacency_list[u].append((v, w))

        dist = {i: float('inf') for i in range(1, n+1)}
        dist[k] = 0

        queue = [(0, k)]

        import heapq

        while queue:
            current_time, node = heapq.heappop(queue)

            if current_time > dist[node]:
                continue

            for v, weight in adjacency_list[node]:
                new_time = current_time + weight
                if new_time < dist[v]:
                    dist[v] = new_time
                    heapq.heappush(queue, (new_time, v))

        max_dist = max(dist.values())

        return max_dist if max_dist < float('inf') else -1
