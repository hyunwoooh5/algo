class Solution:
    def find(self, parent, i):
        root = i
        while parent[root]!=root:
            root = parent[root]

        while parent[i] !=root:
            next_node = parent[i]
            parent[i] = root
            i = next_node
        
        return root

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] +=1
        

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        new_edges = []
        for i, (u, v, w) in enumerate(edges):
            new_edges.append([u, v, w, i])
        
        new_edges.sort(key=lambda x: x[2])

        def get_mst(n, edges, skip_idx=-1, force_idx=-1):
            parent = list(range(n))
            rank = [0] * n
            weight = 0
            count = 0
            
            if force_idx != -1:
                for u, v, w, i in edges:
                    if i == force_idx:
                        self.union(parent, rank, u, v)
                        weight += w
                        count += 1
                        break
                        
            for u, v, w, i in edges:
                if i == skip_idx: continue
                if self.find(parent, u) != self.find(parent, v):
                    self.union(parent, rank, u, v)
                    weight += w
                    count += 1
            
            return weight if count == n - 1 else float('inf')

        std_weight = get_mst(n, new_edges)

        critical, pseudo = [], []

        for i in range(len(edges)):
            if get_mst(n, new_edges, skip_idx=i) > std_weight:
                critical.append(i)

            elif get_mst(n, new_edges, force_idx=i) == std_weight:
                pseudo.append(i)

        return [critical, pseudo]