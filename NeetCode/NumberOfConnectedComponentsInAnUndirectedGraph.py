class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(i):
            root = i

            while parent[root] != root:
                root = parent[root]

            while parent[i] != root:
                next_node = parent[i]
                parent[i] = root
                i = next_node

            return root

        def union(x, y):
            rootx = find(x)
            rooty = find(y)

            if rootx != rooty:
                parent[rootx] = rooty

        for u, v in edges:
            union(u, v)

        ans = set()

        for i in range(n):
            ans.add(find(i))

        return len(ans)


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(i):
            root = i

            while parent[root] != root:
                root = parent[root]

            while parent[i] != root:
                next_node = parent[i]
                parent[i] = root
                i = next_node

            return root

        def union(x, y):
            rootx = find(x)
            rooty = find(y)

            if rootx != rooty:
                parent[rootx] = rooty
                return True
            return False

        ans = n

        for u, v in edges:
            if union(u, v):
                ans -= 1

        return ans
