class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj = [set() for _ in range(n)]

        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        visited = set()

        def dfs(curr, parent):
            visited.add(curr)

            for neighbor in adj[curr]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                if not dfs(neighbor, curr):
                    return False
            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n
