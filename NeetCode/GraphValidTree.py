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


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj_list = [[] for _ in range(n)]

        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        visit = set()

        def dfs(curr, prev):
            if curr in visit:
                return True  # cycle

            visit.add(curr)

            for node in adj_list[curr]:
                if node == prev:
                    continue
                if dfs(node, curr):
                    return True

            return False

        # dfs(0, -1) # true then cycle
        return not dfs(0, -1) and len(visit) == n
