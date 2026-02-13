"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}

        def dfs(current_node):
            if current_node in old_to_new:
                return old_to_new[current_node]

            copy = Node(current_node.val)
            old_to_new[current_node] = copy

            for neighbor in current_node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}
        old_to_new[node] = Node(node.val)
        q = deque([node])

        while q:
            current_node = q.popleft()
            for n in current_node.neighbors:
                if n not in old_to_new:
                    old_to_new[n] = Node(n.val)
                    q.append(n)
                old_to_new[current_node].neighbors.append(old_to_new[n])

        return old_to_new[node]
