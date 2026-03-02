# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, target):
            if not node:
                return False

            target -= node.val
            if not node.left and not node.right:
                return target == 0

            return dfs(node.left, target) or dfs(node.right, target)

        return dfs(root, targetSum)


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val
        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum) or
                (not targetSum and not root.left and not root.right))


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, targetSum - root.val)]
        while stack:
            node, curr_sum = stack.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                stack.append((node.right, curr_sum - node.right.val))
            if node.left:
                stack.append((node.left, curr_sum - node.left.val))

        return False


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        from collections import deque
        queue = deque([(root, targetSum - root.val)])

        while queue:
            node, curr_sum = queue.popleft()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.left:
                queue.append((node.left, curr_sum - node.left.val))
            if node.right:
                queue.append((node.right, curr_sum - node.right.val))

        return False


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, s):
            if not node:
                return False

            s += node.val

            if not node.left and not node.right:
                return s == targetSum

            return dfs(node.left, s) or dfs(node.right, s)

        return dfs(root, 0)


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum) or (targetSum == 0 and not root.left and not root.right)


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # DFS
        stack = [(root, targetSum-root.val)]

        while stack:
            node, curr = stack.pop()

            if not node.left and not node.right and curr == 0:
                return True

            if node.left:
                stack.append((node.left, curr-node.left.val))

            if node.right:
                stack.append((node.right, curr - node.right.val))

        return False


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # BFS
        from collections import deque

        queue = deque([(root, targetSum-root.val)])

        while queue:
            node, curr = queue.popleft()

            if not node.left and not node.right and curr == 0:
                return True

            if node.left:
                queue.append((node.left, curr-node.left.val))

            if node.right:
                queue.append((node.right, curr - node.right.val))

        return False
