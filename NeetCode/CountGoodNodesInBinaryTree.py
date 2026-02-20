# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, m=-100):
            if not node:
                return None

            if node.val >= m:
                self.count += 1
                m = node.val

            dfs(node.left, m)
            dfs(node.right, m)

        dfs(root)

        return self.count


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        from collections import deque
        q = deque()

        q.append((root, -float("inf")))

        while q:
            node, maxval = q.popleft()

            if node.val >= maxval:
                res += 1
                maxval = node.val

            if node.left:
                q.append((node.left, maxval))

            if node.right:
                q.append((node.right, maxval))

        return res
