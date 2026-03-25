# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root1, root2):
            if not root1 and root2:
                return False
            elif root1 and not root2:
                return False
            elif not root1 and not root2:
                return True

            return dfs(root1.left, root2.left) and dfs(root1.right, root2.right) and root1.val == root2.val

        return dfs(p, q)


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root1, root2):
            if not root1 and root2:
                return False
            elif root1 and not root2:
                return False
            elif not root1 and not root2:
                return True

            return root1.val == root2.val and dfs(root1.left, root2.left) and dfs(root1.right, root2.right)

        return dfs(p, q)


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        from collections import deque

        queue1 = deque([p])
        queue2 = deque([q])

        while queue1 and queue2:
            l1, l2 = len(queue1), len(queue2)

            if l1 != l2:
                return False

            for _ in range(l1):
                node1 = queue1.popleft()
                node2 = queue2.popleft()

                if not node1 and not node2:
                    continue

                if not node1 or not node2 or node1.val != node2.val:
                    return False

                queue1.append(node1.left)
                queue1.append(node1.right)
                queue2.append(node2.left)
                queue2.append(node2.right)

        return True
