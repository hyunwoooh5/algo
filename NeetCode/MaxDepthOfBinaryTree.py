# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        count = 0

        from collections import deque

        queue = deque([root])

        while queue:
            length = len(queue)

            for _ in range(length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            count += 1

        return count


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        stack = [[root, 1]]

        ans = 0

        while stack:
            node, depth = stack.pop()

            if node:
                ans = max(ans, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])

        return ans
