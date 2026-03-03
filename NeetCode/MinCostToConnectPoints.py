class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        visited = [False]*n

        min_heap = [(0, 0)]
        total = 0
        nodes_connected = 0

        import heapq

        while nodes_connected < n:
            cost, curr = heapq.heappop(min_heap)

            if visited[curr]:
                continue
            
            # Include current node to MST
            visited[curr] = True
            total += cost
            nodes_connected += 1

            # Calculate distance from current node to unvisited nodes
            for next_node in range(n):
                if not visited[next_node]:
                    dist = abs(points[curr][0]-points[next_node][0]) + \
                        abs(points[curr][1]-points[next_node][1])

                    heapq.heappush(min_heap, (dist, next_node))

        return total
