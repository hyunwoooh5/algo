class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {i: [] for i in range(n)}

        for i in range(len(edges)):
            a, b = edges[i]
            prob = succProb[i]

            adj[a].append((b, prob))
            adj[b].append((a, prob))

        probs = {i: 0 for i in range(n)}

        probs[start_node] = 1.0

        max_heap = [(-1.0, start_node)]

        import heapq

        while max_heap:
            curr, u = heapq.heappop(max_heap)

            curr = -curr

            if u == end_node:
                return curr

            for v, p in adj[u]:
                new = curr * p

                if new > probs[v]:
                    probs[v] = new
                    heapq.heappush(max_heap, (-new, v))

        return 0.0
